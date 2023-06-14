from pandas import read_csv

def extract_data():
    path = [get_directory(dataset) for dataset in ("employees", "timesheets")]
    datasets = [read_csv(_) for _ in path]

    return datasets

def get_directory(dataset: str) -> str:
    base_dir = "~/mekari-de-assignment/data/"
    return base_dir + dataset + ".csv"
