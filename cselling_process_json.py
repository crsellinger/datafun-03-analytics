"""
Process a JSON file to pull pokemon names and save the result.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"
input_filename: str = "pokedex.json"
output_filename: str = "Pokemon.txt"

#####################################
# Define Functions
#####################################


def get_pokemon(file_path: pathlib.Path) -> dict:
    """
    Pull Pokemon names out of json file. 
    """
    with file_path.open("r", encoding="utf-8") as file:
        pokedex = json.load(file)
        # loads as list of dictionaries
        name_list: list = []
        english_name: list = []
        i = 0
        for dict in pokedex:
            # goes through every dictionary in the pokedex list and appends the name sub-dictionary to name_list
            name_list.append(dict["name"])
            # gets value of each english key and appends it to english_name list
            english_name.append(name_list[i].get("english"))
            i += 1
        return english_name


def process_json_file():
    """
    Processes json file by pulling all pokemon names and how many pokemon are in the pokedex. Saves data to folder.
    """
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, input_filename)
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, output_filename)

    pokemon_name = get_pokemon(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as file:
        file.write(f"Number of Pokemon: {len(pokemon_name)}\n")
        file.write(f"Pokemon:\n{pokemon_name}")

    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")


#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
