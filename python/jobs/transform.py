import duckdb
from utils import etl_scripts
from datetime import date, timedelta
from resources import resources


def transform_data(dataframes: tuple):
    if dataframes is None:
        print("Dataframe does not exist in the directory. Please check data.")
    else:
        print("Transforming data...")
        employees, timesheets = dataframes
        transformation_query = get_transformation_query("salary_per_month_query")
        transformed_data = duckdb.query(transformation_query).to_df()

        get_problematic_data(timesheets)

        return transformed_data


def get_problematic_data(dataframe):
    base_dir = resources.resources.get("base_dir")
    save_dir = base_dir + "problematic_data.csv"
    timesheets = dataframe
    troubleshooting_query = get_transformation_query("troubleshooting_query")

    problematic_data = duckdb.query(troubleshooting_query).to_df()
    problematic_data.to_csv(save_dir)

    if len(problematic_data) > 0:
        count_problematic_data = len(problematic_data)
        print(f"WARNING: There are {count_problematic_data} data points being ignored because of invalid check-in/check-out time. Please check {save_dir}")


def get_transformation_query(query_type) -> str:
    today_date = date.today()
    yesterday_date = today_date - timedelta(days=1)
    yesterday_month = yesterday_date.replace(day=1)

    transformation_query = etl_scripts.queries.get(query_type).format(
        YESTERDAY_DATE=yesterday_month.strftime("%Y-%m-%d")
    )

    return transformation_query
