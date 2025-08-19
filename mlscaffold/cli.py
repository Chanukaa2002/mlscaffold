import argparse
import sys
from pathlib import Path

from .templates import (
    WORKFLOW_TXT,
    README_TEMPLATE,
    MAIN_PY_TEMPLATE,
    REQUIREMENTS_TXT,
    GITIGNORE_TXT,
    TEST_SAMPLE,
)

TEMPLATE_DIRS = [
    "src",
    "data/raw",
    "data/processed",
    "models",
    "notebooks",
    "docs",
    "tests",
]


def write_file(path: Path, content: str) -> None:
    """Create parent dirs and write text content to a file (UTF-8)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def create_project(project_name: str, gitignore: bool = True) -> Path:
    """
    Create a new ML project scaffold.

    Parameters
    ----------
    project_name : str
        Name or path for the project directory to create.
    gitignore : bool
        Whether to create a .gitignore file.

    Returns
    -------
    Path
        Absolute path to the created project root.
    """
    root = Path(project_name).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    # 1) Directories
    for d in TEMPLATE_DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)

    # 2) Files
    write_file(root / "README.md", README_TEMPLATE.format(project_name=root.name))
    write_file(root / "requirements.txt", REQUIREMENTS_TXT)
    write_file(root / "ML_Workflow.txt", WORKFLOW_TXT)

    write_file(root / "src" / "__init__.py", "")
    write_file(root / "src" / "main.py", MAIN_PY_TEMPLATE)

    write_file(root / "tests" / "test_smoke.py", TEST_SAMPLE)

    if gitignore:
        write_file(root / ".gitignore", GITIGNORE_TXT)

    print(f"✅ ML project '{root.name}' created at: {root}")
    print(f"👉 Next: cd {root.name}")
    return root


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="mlscaffold",
        description="Create a ready-to-use ML project structure."
    )
    parser.add_argument("name", help="Project name or path to create.")
    parser.add_argument(
        "--no-gitignore",
        action="store_true",
        help="Do not create a .gitignore file."
    )
    return parser.parse_args(argv)


def main():
    args = parse_args(sys.argv[1:])
    try:
        create_project(args.name, gitignore=not args.no_gitignore)
    except Exception as e:
        # Print a clean error and exit non-zero for CLI correctness
        print(f"❌ Error: {e}")
        sys.exit(1)
