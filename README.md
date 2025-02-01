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
Retrieves an excel file filled with data on adult income.

cselling_get_csv.py
Retrieves a comma sepatated values file with air quality data from 2016.

cselling_get_json.py
Retrieves a JSON file of Pokemon data.

cselling_get_text.py
Retrieves a text file of GDP data.

### Command for Fetchers
```shell
py .\cselling_get_excel.py
py .\cselling_get_csv.py
py '.\JSON Getter\cselling_get_json.py'
py .\cselling_get_text.py
```

### Data Processors
cselling_process_excel.py
Processes file to find the mean age in the data set and their average income.

cselling_process_csv.py
Processes fetched file to find temperature statistics.

cselling_process_json.py
Processes fetched file to find all Pokemon names and how many Pokemon are in the data set.

cselling_process_text.py
Processes fetched file to find highest, lowest, and average GDP.\

### Command for Data Processors
```shell
py .\cselling_process_excel.py
py .\cselling_process_csv.py
py .\cselling_process_json.py
py .\cselling_process_text.py
```

