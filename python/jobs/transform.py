import duckdb
from utils import etl_scripts
from datetime import date, timedelta


def transform_data(dataframes: tuple):
    if dataframes is None:
        print("Dataframe does not exist in the directory. Please check data.")
    else:
        print("Transforming data...")
        employees, timesheets = dataframes
        transformation_query = get_transformation_query()
        transformed_data = duckdb.query(transformation_query).to_df()

        return transformed_data


def get_transformation_query() -> str:
    today_date = date.today()
    yesterday_date = today_date - timedelta(days=1)
    yesterday_month = yesterday_date.replace(day=1)
    transformation_query = etl_scripts.GET_SALARY_PER_MONTH.format(
        TODAY_DATE=yesterday_month.strftime("%Y-%m-%d")
    )

    return transformation_query
