import duckdb
from utils import etl_scripts
from datetime import date

def transform_data(dataframes: tuple) -> DataFrame:
    employees, timesheets = dataframes
    transformation_query = get_transformation_query()
    transformed_data = duckdb.query(transformation_query).to_df()

    print(transformed_data)


def get_transformation_query() -> str:
    today_date = date.today()
    transformation_query = etl_scripts.GET_SALARY_PER_MONTH.format(TODAY_DATE = today_date.strftime("%Y-%m-%d"))

    return transformation_query