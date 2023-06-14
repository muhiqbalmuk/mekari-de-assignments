from pandas import read_csv


def extract_data(datasets: tuple) -> tuple:
    path = map(get_directory, datasets)
    print("Extracting data...")
    try:
        dataframes = tuple(map(read_csv, path))
        return dataframes
    except FileNotFoundError:
        print("Please ensure the file exist.")


def get_directory(dataset: str) -> str:
    base_dir = "~/mekari-de-assignment/data/"
    return base_dir + dataset + ".csv"
