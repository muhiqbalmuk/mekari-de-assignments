import duckdb


def load_data_to_csv(transformed_data):
    salary_per_hour_per_month = transformed_data
    duckdb.sql(
        """INSERT INTO OR REPLACE salary_per_month SELECT * FROM salary_per_hour_per_month"""
    )
