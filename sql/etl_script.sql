-- POPULATING BASE TABLE ACCORDING TO NEWLY-ARRIVED DATA
TRUNCATE main.timesheets;
TRUNCATE main.employees;
INSERT INTO timesheets SELECT * FROM read_csv_auto('~/mekari-de-assignment/data/timesheets.csv');
INSERT INTO employees SELECT * FROM read_csv_auto('~/mekari-de-assignment/data/employees.csv');

-- CONDUCTING THE TRANSFORMATION AND LOAD INTO STAGE TABLE
CREATE TABLE main.stage_salary_per_hour AS
WITH wrangled_data AS (
    SELECT
        timesheets.employee_id
        , employees.branch_id
        , employees.salary
        , date_trunc('month', timesheets."date") as timesheet_month
        , timesheets.checkin
        , timesheets.checkout
        , ROUND(date_diff('minutes', timesheets.checkin, timesheets.checkout) / 60) as workhours
    FROM main.timesheets AS timesheets
    LEFT JOIN main.employees AS employees
        ON timesheets.employee_id = employees.employe_id
    WHERE timesheets.checkin IS NOT NULL AND timesheets.checkout IS NOT NULL
)

SELECT
    timesheet_month
    , branch_id
    , sum(salary) AS total_salary
    , sum(workhours) AS total_workhours
    , ROUND(sum(salary) / sum(workhours), 2) AS total_salary_per_hour
FROM wrangled_data
GROUP BY
    timesheet_month
    , branch_id;

-- REPOPULATE THE TARGET TABLE SINCE IT IS FULL-LOAD TRANSFORMATION
TRUNCATE salary_per_hour;
INSERT INTO salary_per_hour SELECT * FROM main.stage_salary_per_hour;

-- DROP THE STAGE TABLE
DROP TABLE stage_salary_per_hour;