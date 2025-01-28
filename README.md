# Datafun Analytics 03

---

## Module 3
*Project Repo for Module 3*

1. clone git repo using `git clone [url]`

2. create a virtual environment using `py -m venv .venv`

## Run Locally - Initial Start

After cloning your project down to your Documents folder, open the project folder for editing in VS Code.

Create a local project virtual environment named .venv, activate it, and install the requirements.

When VS Code asks to use it for the workspace, select Yes.
If you miss the window, after installing, select from the VS Code menu, View / Command Palette, and type "Python: Select Interpreter" and select the .venv folder.

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands (for Windows - the activate command is slightly different Linux/Mac).

```shell
.venv\Scripts\Activate
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```

## How to Push Changes Back to GitHub

Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
git add .
git commit -m "Useful commit message"
git push -u origin main
```

### Fetchers
cselling_get_excel.py


cselling_get_csv.py


cselling_get_json.py


cselling_get_text.py

### Command for Fetchers


### Data Processors
cselling_process_excel.py


cselling_process_csv.py


cselling_process_json.py


cselling_process_text.py

### Command for Data Processors


