import pandas as pd
import numpy as np

np.random.seed(42)
n=1000

study_hours = np.random.randint(0,12,n)
attendance = np.random.randint(40,100,n)
prev_marks = np.random.randint(30,100,n)
assignments = np.random.randint(0,10,n)
sleep_hours = np.random.randint(3,10,n)
internet_hours = np.random.randint(0,8,n)

score = (study_hours*4 + attendance*0.4 +prev_marks*0.3 + assignments*3 + sleep_hours*2
 - internet_hours*2)

result=[]
for s in score:
    if s > 130:
        result.append("High")
    elif s > 90:
        result.append("Medium")
    else:
        result.append("Low")


df= pd.DataFrame({
    'StudyHours':study_hours,
    'Attendace':attendance,
    'PreviousMarks':prev_marks,
    'Assignments':assignments,
    'SleepHours':sleep_hours,
    'InternetHours':internet_hours,
    'Result':result
})
df.to_csv('student_data.csv',index=False)
print("Dataset created successfully")
print(df.head())
print("Total rows:",len(df))
print("Result distribution:")
print(df['Result'].value_counts())





