# mekari-de-assignments

This assignment comes in two parts: SQL and Python.

Some specs:
1. The DB used for this task is duckdb (duckdb.org)
2. The python version used in this task is 3.10.11 64-bit
3. All the required packages are inside python/requirements.txt
4. Data is stored in data/ folder
5. SQL script is stored in sql/
6. Python script is stored in python/


Assumptions made:
1. For python case, it is assumed the raw csv data is being appended/updated (i.e., it will contain the old data also) and each day will contain data up to D-1.
2. It's also assumed that only timesheets and employees data are being considered, i.e., if there is another table needed to conduct the transformation, the python script will also need some updates.

Important caveats:
1. In the transformation, data points where check-in or check-out time is null is being ignored. This is done because the analysis is to be made on the branch level and the data points where such condition occur only happens at 2.5% of the overall dataset, so ignoring this should not hamper analysis on branch level. The code will also send a warning how many data points are being ignored on a given day and store the problematic data points in a separate csv file.
