from jobs import extract, transform, load

def main():
    datasets = ("employees", "timesheets")

    dataframes = extract.extract_data(datasets)
    salary_per_hour = transform.transform_data(dataframes)
    # load(salary_per_hour)

if __name__ == "__main__":
    main()
