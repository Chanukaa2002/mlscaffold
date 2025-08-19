# 🤝 Contributing to mlscaffold

Thank you for your interest in contributing! 🎉  
We welcome developers, data scientists, and ML enthusiasts to improve this project.

---

## 📌 How to Contribute

1. **Fork the repository**  
   Use GitHub’s fork button.

2. **Clone your fork**  
```bash
git clone https://github.com/<your-username>/mlscaffold.git
cd mlscaffold
```
3. **Create a new branch**

* Use your initials for the prefix.
* Format: < initials >/feature/feature-name or < initials >/hotfix/hotfix-name
Example for "Chanuka Dilshan":
```bash
git checkout -b <CD>/feature/feature-name
# or
git checkout -b <CD>/hotfix/hotfix-name
```
4. **Install locally**
```bash
python -m venv .venv
# Activate environment
# Linux/Mac:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -e .
```
5. **Make your changes**

* Follow PEP8 coding style

* Add new templates, options, or workflow improvements

* Keep code clean and documented

6. **Test your changes**

```
mlscaffold demo-project
cd demo-project
python src/main.py
```

7. **Write a clean commit message**

* Use conventional commit messages:

    * feat: → new feature

    * fix: → bug fix

    * docs: → documentation

    * refactor: → code refactor

    * test: → tests

    Example:
    ```
    feat: add --no-gitignore option
    ```

8. **Push and open Pull Request**

```
git push origin <your-name>/feature/feature-name
```