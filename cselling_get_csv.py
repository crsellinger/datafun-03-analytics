"""
Caleb Sellinger
Dr. Case
44608, Data Analytics Fundamentals

Getter function for retrieving .csv file from web
"""

import pathlib
import requests
from utils_logger import logger

fetched_folder_name = "something lalala"

def get_csv(save_folder: str, filename: str, url: str) -> None:
    """
    Retrieve .csv file from given URL, write to new file, and save to named folder.

    Arguments:
    save_folder -- Name of folder to save to.
    filename -- Name of file to retrieve.
    url -- URL of .csv file to retrieve. Where to retrieve .csv file from.

    Returns: None
    """
    if not url:
        logger.error("The URL provided is empty or does not exist. Please provide a valid URL.")
        return
    
    try:
        logger.info(f"Retrieving CSV file from {url}...")

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error: {req_err}")

def write_csv(save_folder:str, filename: str, csv_data: str) -> None:
    """
    Write .csv file to new file and save to folder.

    Arguments:
    save_folder -- Name of folder to save to.
    filename -- Name of file to retrieve.
    csv_data -- .csv content as string.

    Returns: None
    """
    file_path = pathlib.Path(save_folder).joinpath(filename)

    try:
        logger.info(f"Writing data to file: {filename}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file = file_path.open('w')
        file.write(csv_data)
        file.close()
        logger.info(f"SUCCESS: data written to new file {filename}")
    except IOError:
        logger.error(f"Error writing to file: {IOError}")

def main():
    """
    Main function for running program
    """
    csv_url = 'something something'
    logger.info("Retrieving file...")
    get_csv(fetched_folder_name, "New File.csv", csv_url)


if __name__ == '__main__':
    main()
