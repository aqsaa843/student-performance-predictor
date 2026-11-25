import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
import pandas as pd

print("Creating data...")

np.random.seed(42)
n = 500
study = np.random.randint(1, 10, n)
attendance = np.random.randint(40, 100, n)
previous = np.random.randint(30, 95, n)
assignment = np.random.randint(40, 100, n)
sleep = np.random.randint(4, 10, n)
social = np.random.randint(0, 7, n)

final = (study*3 + attendance*0.3 + previous*0.4 + assignment*0.1 - social*2 + sleep*1)
final = np.clip(final, 0, 100)

X = np.column_stack([study, attendance, previous, assignment, sleep, social])
y = final

# Save correct CSV also for viva
df = pd.DataFrame(X, columns=['study_hours','attendance','previous_marks','assignment','sleep_hours','social_hours'])
df['final_marks'] = y
df.to_csv('student_data.csv', index=False)
print("student_data.csv fixed!")

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

with open('model.pkl','wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")