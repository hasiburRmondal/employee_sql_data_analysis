import pandas as pd
from sqlalchemy import create_engine

db_url = 'mysql+pymysql://root:@localhost:3306/employee_sql_data_analysis'
engine = create_engine(db_url)

# ================Get 5 rows from the employee table==================
# query = 'SELECT * FROM employee LIMIT 5'
# df = pd.read_sql(query, engine)
# print(df)
# -------------Or---------------------
# df = pd.read_sql(query, engine)
# print(df.head())

# ================Get Employee Count in Each Department==================
# query = 'SELECT DISTINCT department, Count(*) AS Total_employee FROM employee GROUP BY department ORDER BY Total_employee DESC' #DISTINCT - to get unique values
# df = pd.read_sql(query, engine)
# print(df)

# ================Get Average Salary of Each Department==================
# query = 'SELECT DISTINCT department, AVG(salary) AS Average_salary FROM employee GROUP BY department ORDER BY Average_salary DESC'
# df = pd.read_sql(query, engine)
# print(df)

# ================Get top 5 highest salary employee==================
# query = 'SELECT FirstName, salary FROM employee ORDER BY salary DESC LIMIT 5'
# df = pd.read_sql(query, engine)  
# print(df)

# ================Get 2nd highest salary employee==================
# query = 'SELECT FirstName, salary FROM employee ORDER BY salary DESC LIMIT 1 OFFSET 1'
# df = pd.read_sql(query, engine)
# print(df)
# ----------------Or using DENSE_RANK() - Common Table Expressions (CTEs)---------------------
# query = 'WITH Ranked_Employee AS (SELECT FirstName, salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS Salary_Rank FROM employee) SELECT FirstName, salary FROM Ranked_Employee WHERE Salary_Rank = 2'
# df = pd.read_sql(query, engine)
# print(df)
# ----------------Or using Subquery---------------------
# # query = 'SELECT MAX(salary) FROM employee WHERE salary < (SELECT Max(salary) FROM employee)'
# query = '''
# SELECT FirstName, salary
# FROM employee
# WHERE salary = (
#     SELECT MAX(salary)
#     FROM employee
#     WHERE salary < (
#         SELECT MAX(salary) FROM employee
#     )
# )
# '''
# df = pd.read_sql(query, engine)
# print(df)