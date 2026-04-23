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

result=table.groupby('dept').agg(
 CountofEmps=('empid','count'),
  Totalsalary=('salary','sum'),
   avgSalary=('salary','mean'),
   minAge=('age','min') 
)
print(result)

# Q)find employee avg experience ,avg age in location wise
result=table.groupby('location').agg(
    avgExperience=('exp','mean'),
    avgAge=('age','mean')
)
print(result)
