-- THIS DDL STATEMENT INITIALISE THE TABLE CREATION
-- DUCKDB DBMS IS BEING USED FOR THIS PROBLEM SET

CREATE TABLE employees AS SELECT * FROM read_csv_auto('~/mekari-de-assignments/data/employees.csv');
CREATE TABLE timesheets AS SELECT * FROM read_csv_auto('~/mekari-de-assignments/data/timesheets.csv');
CREATE TABLE salary_per_hour (
    timesheet_month DATE,
    branch_id BIGINT,
    total_salary HUGEINT,
    total_workhours BIGINT,
    total_salary_per_hour DOUBLE
);