import argparse
import sys
import shutil
from pathlib import Path
import questionary

from .templates import (
    WORKFLOW_TXT,
    README_TEMPLATE,
    MAIN_PY_TEMPLATE,
    REQUIREMENTS_TXT,
    GITIGNORE_TXT,
    TEST_SAMPLE,
)

# Define directory structures per template
TEMPLATES = {
    "basic": [
        "src",
        "data",
        "models",
        "notebooks",
    ],
    "research": [
        "src",
        "data/raw",
        "data/processed",
        "models",
        "notebooks",
        "docs",
        "experiments",
        "tests",
    ],
    "production": [
        "src",
        "data",
        "models",
        "notebooks",
        "docs",
        "api",
        "tests",
        ".github/workflows",
    ],
}

def write_file(path: Path, content: str) -> None:
    """Create parent dirs and write text content to a file (UTF-8)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def create_project(project_name: str, template: str, gitignore: bool = True) -> Path:
    """
    Create a new ML project scaffold.
    """
    root = Path(project_name).expanduser().resolve()
    if root.exists():
        print(f"❌ Project '{project_name}' already exists.")
        return root

    root.mkdir(parents=True, exist_ok=True)

    for d in TEMPLATES[template]:
        (root / d).mkdir(parents=True, exist_ok=True)

    write_file(root / "README.md", README_TEMPLATE.format(project_name=root.name))
    write_file(root / "requirements.txt", REQUIREMENTS_TXT)
    write_file(root / "ML_Workflow.txt", WORKFLOW_TXT)

    write_file(root / "src" / "__init__.py", "")
    write_file(root / "src" / "main.py", MAIN_PY_TEMPLATE)

    if "tests" in TEMPLATES[template]:
        write_file(root / "tests" / "test_smoke.py", TEST_SAMPLE)

    if gitignore:
        write_file(root / ".gitignore", GITIGNORE_TXT)

    if template == "production":
        write_file(
            root / "Dockerfile",
            "FROM python:3.9\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD [\"python\", \"src/main.py\"]"
        )
        # GitHub Actions
        ci_file = root / ".github" / "workflows" / "ci.yml"
        write_file(
            ci_file,
            "name: CI\non: [push]\njobs:\n  build:\n    runs-on: ubuntu-latest\n"
            "    steps:\n      - uses: actions/checkout@v2\n"
            "      - uses: actions/setup-python@v2\n        with:\n          python-version: 3.9\n"
            "      - run: pip install -r requirements.txt\n      - run: pytest\n"
        )

    print(f"✅ ML project '{root.name}' created at: {root}")
    print(f"👉 Next: cd {root.name}")
    return root


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="mlscaffold",
        description="Create a ready-to-use ML project structure."
    )
    parser.add_argument("name", help="Project name or path to create.")
    return parser.parse_args(argv)


def main():
    args = parse_args(sys.argv[1:])
    custom_style = questionary.Style([
        ("qmark", "fg:#673ab7 bold"),       
        ("question", "bold"),               
        ("selected", "fg:#03dac6 bold"),    
        ("pointer", "fg:#ff5722 bold"),     
        ("answer", "fg:#ff9800 bold")
    ])

    template = questionary.select(
        "Choose project type:",
        choices=["basic", "research", "production"],
        style=custom_style
    ).ask()

    include_gitignore = questionary.confirm(
        "Do you want to include a .gitignore?"
    ).ask()

    try:
        create_project(args.name, template=template, gitignore=include_gitignore)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()