"""
Process a text file to find statistics for GDP per capita and save result to data_processed folder.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib

# Import from local project modules
from utils_logger import logger

import statistics

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"
input_filename: str = "GDP per Capita.txt"
output_filename: str = "GDP.txt"

#####################################
# Define Functions
#####################################


def stats_gdp(file_path: pathlib.Path) -> int:
    """
    Gets max, min, and mean GDP per Capita in text file.
    """
    data: list = []
    gdp_list: list = []
    # max: int = 0
    j: int = 0
    # try:
    with file_path.open("r") as file:
        for i in file:
            line = i.split()
            data.append(line)
            gdp_list.append(int(data[j][-1].replace(",", "")))
            j += 1
        x = max(gdp_list)
        y = min(gdp_list)
        z = round(statistics.mean(gdp_list), 0)
        return x, y, z
    # except Exception as e:
    #     logger.error(f"Error reading text file: {e}")
    #     return 0


def process_text_file():
    """
    Read a text file, parse input file for numbers, calculate stats, and save file to folder.
    """
    input_file = pathlib.Path(fetched_folder_name, input_filename)
    output_file = pathlib.Path(processed_folder_name, output_filename)
    max, min, mean = stats_gdp(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w") as file:
        file.write(f"Highest GDP: {max}\nLowest: GDP: {min}\nMean GDP: {mean}")
    logger.info(f"Processed text file: {input_file}. Data saved to {output_file}")


#####################################
# Main Execution
#####################################

def main():
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")

if __name__ == "__main__":
    main()
