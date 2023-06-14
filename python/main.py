from jobs import extract, transform, load


def main():
    datasets = ("employees", "timesheets")

    dataframes = extract.extract_data(datasets)
    salary_per_hour = transform.transform_data(dataframes)

    if len(salary_per_hour) > 0:
        load.load_data_to_csv(salary_per_hour)
    else:
        print(
            "Either no update for the existing data or the current data does not contain updated data. Please check the data."
        )


if __name__ == "__main__":
    main()
