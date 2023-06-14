from pandas import read_csv

def extract_data(datasets: tuple) -> tuple:
    path = map(get_directory, datasets)
    dataframes = tuple(map(read_csv, path))

    return dataframes

def get_directory(dataset: str) -> str:
    base_dir = "~/mekari-de-assignment/data/"
    return base_dir + dataset + ".csv"
