import pandas as pd
# table = pd.read_csv("Indian_Traffic_Violations.csv") 

# print(table)
# print(table.columns)


# print(table[["Fine _Amount","Vehicle_Model_year"]])
# new=(table[["Fine_Amount","Vehicle_Model_year"]])
# print(new)

# print(table['Violation_Type'])
# result = table[table['Violation_Type']=='No Seatbelt']
# # print(result)
# result=table [table['Vehicle_Model_Year']>=2018]
# print(result)


# Task 3
# Q)write a pgm to find the electricity bill
# notes:if your usage is below 100 unit,it is free
#  if your usage is btw 100&200,pay 2 rupees/unit on above 100 unit                                                                
# if  your usage is above 200 pay 5 rupees/unit above 200 unit


# # units=int(input("Enter electricity usage(units):"))
# if units <= 100:
#     bill=0
# elif units <=200:
#     bill=(units-100)*2
# else:
#     bill=(100*2)+(units-200)*5
# print("Electricity Bill=",bill)

# Q)find violations from location Maharashtra
# Q)find violations by driver age below 30

# result_location=table[table[table['Location']=='maharasthra']
# print(result_Location)]
# result_age=table[table[table['driver_Age']='<30'
# print(result_age)


studentTable=pd.read_csv('students.csv')
print(studentTable)
print(studentTable['name'])
print(studentTable[['name','mark']])
result=studentTable[ studentTable['mark']<=575]
print(result) 
# syntax:table[()&()&()]
result=studentTable[(studentTable['mark']<=570)&(studentTable['age']>=20)]
print(result)
result=studentTable[studentTable['mark']<=570|(studentTable['age']>=20)]
print(result)

# Q)find student with mark above 560 and below 575
# result=studentTable[(studentTable['mark'])]





























































































































