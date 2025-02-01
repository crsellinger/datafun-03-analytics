"""
Process an Excel file to count occurrences of a specific word in a column.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import openpyxl

# Import from local project modules
from utils_logger import logger

import statistics

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"
data_file: str = "Income Census.xlsx"
output_file_name: str = "Income Census.txt"

#####################################
# Define Functions
#####################################


def stats_income(file_path: pathlib.Path) -> int:
    """Count the occurrences of a specific word in a given column of an Excel file."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    # age = []
    # cell = 1
    # for cell in sheet["A"]:
    #     age.append(cell.value)

    # list comprehension of for loop above
    ages = [age.value for age in sheet["A"]]

    # del age[0]
    del ages[0]

    mean = round(statistics.mean(ages),0)

    i = ages.index(mean)
    # i + 2 to account for header and sheet rows start at 1 instead of 0
    row_vals = [cell.value for cell in sheet[i+2]]

    return mean, row_vals[14]
    # for cell in sheet:


def process_excel_file():
    """Read an Excel file, count occurrences of 'GitHub' in a specific column, and save the result."""
    input_file = pathlib.Path(fetched_folder_name, data_file)
    output_file = pathlib.Path(processed_folder_name, output_file_name)

    mean, income = stats_income(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w") as file:
        file.write(f"Mean Age: {mean}\nMean Income: {income}\n")
    logger.info(f"Processed Excel file: {input_file}\n")


#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")
