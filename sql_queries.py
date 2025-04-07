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

# ================Get Department Wise Total Employee==================
query = 'SELECT DISTINCT department, Count(*) AS Total_employee FROM employee GROUP BY department ORDER BY Total_employee DESC' #DISTINCT - to get unique values
df = pd.read_sql(query, engine)
print(df)
