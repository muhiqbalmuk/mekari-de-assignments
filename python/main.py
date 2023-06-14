from jobs import extract, transform, load

def main():
    dataset = extract.extract_data()
    # salary_per_hour = transform(dataset)
    # load(salary_per_hour)

if __name__ == "__main__":
    main()
