import pandas as pd
table=pd.read_csv("Teen_Mental_Health_Dataset.csv")
#Q1) find average daily social media hours grouped by gender
# result=table.groupby('gender')['daily_social_media_hours'].mean()
# print(result)


# Q2)  find average sleep hours for each platform_usage(instagram,TikTok,Both)
# result=table.groupby('platform_usage')['sleep_hours'].mean()
# print(result)

# Q3)find mean academic performance grouped by social_interaction_level
# result=table.groupby('social_interaction_level')['academic_performance'].mean()
# print(result)


# Q4)find maximum stress_level for each gender
# result=table.groupby('gender')['stress_level'].max()
# print(result)

# Q5)group users based on screen_time_before_sleep and find average sleep_hours and anxiety_level
# table['screen_group']=pd.cut(table['screen_time_before_sleep'],bins=[0,1,2,3],
# labels=['low','medium','high'])
# result=table.groupby('screen_group')[['sleep_hours','anxiety_level']].mean()
# print(result)

# Q6)find total physical_activity grouped by gender
# result=table.groupby('gender')['physical_activity'].sum()
# print(result)

# Q7)count number of students in each social_interaction_level
# result=table['social_interaction_level'].value_counts()
# print(result)

# Q8)find average anxiety_level grouped by platform_usage
# result=table.groupby('platform_usage')['anxiety_level'].mean()
# print(result)

# Q9)find maximum sleep hours among students with high stress_level
# result=table[table['stress_level']>7]['sleep_hours'].min()
# print(result)

# Q10)total addiction_level for each social_interaction_level
result=table.groupby('social_interaction_level')['addiction_level'].sum()
print(result)