# 🚀 mlscaffold

`mlscaffold` is a Python CLI tool to **bootstrap Machine Learning projects** quickly.  
It creates a clean folder structure, boilerplate files, and an ML workflow checklist, so you can start coding immediately.

Think of it as `create-react-app` — but for ML projects.

---

## ✨ Features

- 📂 Automatically generates a standard ML project structure
- 📝 Includes `ML_Workflow.txt` for step-by-step guidance
- ⚡ Boilerplate folders and files:
  - `src/` → Python source code (`main.py`, `__init__.py`)
  - `data/raw` & `data/processed` → Data storage
  - `models/` → Trained models
  - `notebooks/` → Jupyter notebooks
  - `docs/` → Project documentation
  - `tests/` → Unit or smoke tests
  - `requirements.txt` → Python dependencies
  - `.gitignore` → Recommended ignores
- 🧑‍💻 Easy to use and extend
- 🔄 Works on **Windows, Linux, and Mac**

---

## 📦 Installation

Clone and install locally:

```bash
git clone https://github.com/yourusername/mlscaffold.git
cd mlscaffold

# create a virtual environment
python -m venv .venv
# activate it
# Linux/Mac:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate
# Windows PowerShell:
.venv\Scripts\Activate.ps1

# install in editable mode
pip install -e .
```
## 🚀 Usage 
Create a new ML project:
```
mlscaffold my-ml-project
```

output
```
✅ ML project 'my-ml-project' created at: /your/path/my-ml-project
👉 Next: cd my-ml-project
```

## 📁 Generated Project Structure

```
my-ml-project/
├─ src/
│  ├─ __init__.py
│  └─ main.py
├─ data/
│  ├─ raw/
│  └─ processed/
├─ models/
├─ notebooks/
├─ docs/
├─ tests/
│  └─ test_smoke.py
├─ ML_Workflow.txt
├─ requirements.txt
├─ README.md
└─ .gitignore
```
ML_Workflow.txt includes the full ML workflow checklist:
```
0) Project setup
1) Problem framing
2) Data collection
3) Preprocessing
4) Exploratory Data Analysis (EDA)
5) Baseline & Models
6) Training & Evaluation
7) Hyperparameter Tuning
8) Packaging & Artifacts
9) Deployment
10) Monitoring & Iteration
```
## 🤝 Contributions
We welcome contributions! Please read CONTRIBUTIONS.md