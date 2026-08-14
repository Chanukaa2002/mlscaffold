# 🚀 mlscaffold

`mlscaffold` is a lightweight Python CLI tool to **bootstrap Machine Learning projects** in seconds.  
It generates a clean folder structure, boilerplate code, tests, and an ML workflow checklist so you can jump straight into data exploration and model development.

Think of it as `create-react-app` — but for Machine Learning.

---

## ✨ Features

- 📂 **Standard Directory Layout**: Pre-configured folders for data, notebooks, models, and source code.
- ⚡ **Boilerplate Code**: Includes starter `main.py`, package initialization, and smoke tests.
- 📝 **Workflow Checklist**: Ships with `ML_Workflow.txt` covering end-to-end ML lifecycle steps.
- 🚫 **Configurable .gitignore**: Includes tailored ignores for Python, data caches, and Jupyter checkpoints (can be disabled).
- 🔄 **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux.

---

## 📦 Quick Installation

Install directly via `pip`:

```bash
pip install mlscaffold
```

---

## 🚀 Usage

Create a new ML project with a single command:

```bash
mlscaffold my_ml_project
```

### Options & Flags

| Flag | Description |
| :--- | :--- |
| `name` | **Required**. The name or path of the new project to create. |
| `--no-gitignore` | Skip creating the default `.gitignore` file. |
| `-h`, `--help` | Show available CLI options and exit. |

#### Example:
```bash
# Create project without .gitignore
mlscaffold my_ml_project --no-gitignore
```

#### Output:
```text
✅ ML project 'my_ml_project' created at: /path/to/my_ml_project
👉 Next: cd my_ml_project
```

---

## 🛠️ Local Installation & Development Setup

If you want to contribute to `mlscaffold` or test changes locally, follow these steps:

### 1. Prerequisites
- Python **3.8+**
- `git`

### 2. Clone the Repository
```bash
git clone https://github.com/Chanukaa2002/mlscaffold.git
cd mlscaffold
```

### 3. Create & Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install in Editable Mode
Install the package in editable mode (`-e`), which links your local source code directly to the environment:

```bash
pip install -e .
```

> **Note**: Any changes you make in `mlscaffold/` will immediately reflect in the CLI without needing a reinstall.

### 5. Run & Test Locally

You can run your local build using either method:

- **Using the CLI command:**
  ```bash
  mlscaffold test_project
  ```

- **Directly as a Python module (without installing CLI):**
  ```bash
  python -m mlscaffold.cli test_project
  ```

### 6. Run Automated Tests
```bash
pip install pytest
pytest
```

---

## 📁 Generated Project Structure

When you create a project, `mlscaffold` generates the following layout:

```text
my_ml_project/
├── data/
│   ├── raw/            # Immutable raw data storage
│   └── processed/      # Cleaned and transformed datasets
├── docs/               # Project documentation and reports
├── models/             # Serialized model weights / checkpoints
├── notebooks/          # Jupyter notebooks for experiments & EDA
├── src/                # Modular Python source code
│   ├── __init__.py
│   └── main.py         # Application entry point
├── tests/              # Unit and integration tests
│   └── test_smoke.py
├── .gitignore          # Preconfigured ignores for Python & ML artifacts
├── ML_Workflow.txt     # Step-by-step ML lifecycle checklist
├── README.md           # Project documentation template
└── requirements.txt    # Python dependencies list
```

---

## 📋 Included ML Workflow Checklist (`ML_Workflow.txt`)

Every scaffolded project includes a 10-step guide for standard ML projects:

1. **Project Setup** — Environment & repository configuration
2. **Problem Framing** — Define metrics, scope, and objectives
3. **Data Collection** — Gather and verify datasets
4. **Preprocessing** — Cleaning, validation, and transformations
5. **Exploratory Data Analysis (EDA)** — Visualizations & feature insights
6. **Baseline & Models** — Establish benchmark models
7. **Training & Evaluation** — Experimentation and metric tracking
8. **Hyperparameter Tuning** — Model optimization
9. **Packaging & Artifacts** — Exporting models & dependencies
10. **Deployment & Monitoring** — Serving and performance tracking

---

## 🤝 Contributing

Contributions are welcome! Please check out [CONTRIBUTIONS.md](file:///e:/projects/mlscaffold/CONTRIBUTIONS.md) for branch naming conventions, workflow guidelines, and pull request steps.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](file:///e:/projects/mlscaffold/LICENSE) for more information.