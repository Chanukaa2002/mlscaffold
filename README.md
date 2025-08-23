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

```bash
pip install mlscaffold
```

## 🚀 Usage 
Create a new ML project:
```
mlscaffold my-ml-project
```

output
```
✅ ML project 'my-ml-project' created at: /your/path/my-ml-project
👉 Next : cd my-ml-project
```

## 📁 Project Structures

`mlscaffold` supports three project types: **basic**, **research**, and **production**. Choose the one that fits your workflow:

### 1. Basic
For quick experiments, prototypes, or simple scripts.
```
my-ml-project/
├─ src/
│  ├─ __init__.py
│  └─ main.py
├─ data/
├─ models/
├─ notebooks/
├─ tests/
│  └─ test_smoke.py
├─ ML_Workflow.txt
├─ requirements.txt
├─ README.md
└─ .gitignore
```

### 2. Research
For academic, research, or more complex projects with experiments and documentation.
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
├─ experiments/
├─ tests/
│  └─ test_smoke.py
├─ ML_Workflow.txt
├─ requirements.txt
├─ README.md
└─ .gitignore
```

### 3. Production
For production-ready ML systems, APIs, and CI/CD integration.
```
my-ml-project/
├─ src/
│  ├─ __init__.py
│  └─ main.py
├─ data/
├─ models/
├─ notebooks/
├─ docs/
├─ api/
├─ tests/
│  └─ test_smoke.py
├─ .github/
│  └─ workflows/
│      └─ ci.yml
├─ Dockerfile
├─ ML_Workflow.txt
├─ requirements.txt
├─ README.md
└─ .gitignore
```

---

`ML_Workflow.txt` includes the full ML workflow checklist:
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