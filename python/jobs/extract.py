from pandas import read_csv
from resources import resources


def extract_data(datasets: tuple) -> tuple:
    path = map(get_directory, datasets)
    print("Extracting data...")
    try:
        dataframes = tuple(map(read_csv, path))
        return dataframes
    except FileNotFoundError:
        print("Please ensure the file exist.")


def get_directory(dataset: str) -> str:
    base_dir = resources.resources.get("base_dir")
    return base_dir + dataset + ".csv"
