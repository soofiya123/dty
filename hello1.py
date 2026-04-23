import pandas as pd
table=pd.read_csv('Employee.csv')
#print (table)

#total salary of employees
print(table['salary'].sum())
print(table['salary'].mean())
print(table['name'].min())
print(table['salary'].max())
print(table['salary'].count())

result=table.agg(
totalsalary=('salary','sum'),
avgsalary=('salary','mean'),
firstEmployee=('name','min'),
lastEmployee=('name','max'),
)
print(result)