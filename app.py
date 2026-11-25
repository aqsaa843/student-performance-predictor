from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model = None
if os.path.exists('model.pkl'):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✅ model.pkl loaded successfully!")
else:
    print("⚠️ model.pkl not found! Run python train_model.py first")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # If user refreshes result page, go back to form - no error
    if request.method == 'GET':
        return render_template('index.html')

    # Get data from form
    study = float(request.form['study_hours'])
    attendance = float(request.form['attendance'])
    previous = float(request.form['previous_marks'])
    assignment = float(request.form['assignment'])
    sleep = float(request.form['sleep_hours'])
    social = float(request.form['social_hours'])

    # Predict using model.pkl
    if model is not None:
        features = np.array([[study, attendance, previous, assignment, sleep, social]])
        prediction = model.predict(features)[0]
    else:
        # Fallback formula if model not found
        prediction = (study*3 + attendance*0.3 + previous*0.4 + assignment*0.1 - social*2 + sleep*1)

    prediction = round(max(0, min(100, prediction)), 1)

    # Message based on prediction
    if prediction >= 85:
        message = "🌟 Excellent! You are a Topper!"
    elif prediction >= 70:
        message = "✅ Very Good! Keep it up!"
    elif prediction >= 50:
        message = "👍 Good! A little more effort = Distinction"
    elif prediction >= 35:
        message = "⚠️ Need to Work Harder"
    else:
        message = "❌ At Risk - Focus on Study & Attendance"

    # For bars in result.html
    w_study = min(100, study * 10)  # 10 hrs = 100%
    w_sleep = min(100, sleep * 12)  # 8 hrs = ~96%

    return render_template('result.html',
        prediction=prediction,
        message=message,
        study=study, attendance=attendance,
        previous=previous, assignment=assignment,
        sleep=sleep, social=social,
        s=study, a=attendance, p=previous,
        asg=assignment, sl=sleep, so=social,
        w_study=w_study, w_sleep=w_sleep
    )

if __name__ == '__main__':
    app.run(debug=True)