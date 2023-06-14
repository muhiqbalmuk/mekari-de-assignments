queries = {
    "salary_per_month_query": """
WITH wrangled_data AS
(
    SELECT
        DATE_TRUNC('month', CAST(timesheets.date AS DATE)) as timesheet_month
        , employees.branch_id
        , employees.salary
        , ROUND(DATE_DIFF('minutes', CAST(timesheets.checkin AS TIME), CAST(timesheets.checkout AS TIME)) / 60) as workhours
    FROM timesheets
    LEFT JOIN employees
        ON timesheets.employee_id = employees.employe_id
    WHERE
        CAST(timesheets."date" AS DATE) >= DATE'{YESTERDAY_DATE}'
        AND timesheets.checkin IS NOT NULL AND timesheets.checkout IS NOT NULL
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
    , branch_id
""",
    "troubleshooting_query": """
    SELECT
        *
    FROM timesheets
    WHERE
        CAST(timesheets."date" AS DATE) = DATE'{YESTERDAY_DATE}'
        AND (timesheets.checkin IS NULL OR timesheets.checkout IS NULL)
    """
}
