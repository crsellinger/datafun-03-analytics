"""
Process a CSV file on Air Quality during 2016 to analyze the `T` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def analyze_T(file_path: pathlib.Path) -> dict:
    """Analyze T column to calculate min, max, mean, and stdev."""
    try:
        # initialize an empty list to store the scores
        T_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    T = float(row["T"])  # Extract and convert to float
                    # append the T to the list
                    T_list.append(T)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min T": min(T_list),
            "max T": max(T_list),
            "mean T": statistics.mean(T_list),
            "stdev T": statistics.stdev(T_list),
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze T, and save the results."""
    input_file = pathlib.Path(fetched_folder_name, "Air Quality 2016.csv")
    output_file = pathlib.Path(processed_folder_name, "Air Quality Results.txt")
    
    stats = analyze_T(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("T Statistics:\n")
        file.write(f"Minimum: {stats['min T']:.2f}\n")
        file.write(f"Maximum: {stats['max T']:.2f}\n")
        file.write(f"Mean: {stats['mean T']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev T']:.2f}\n")
    
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")