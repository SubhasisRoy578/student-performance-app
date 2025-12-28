from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        # ---------- Read inputs ----------
        study_hours = float(request.form['study_hours'])
        attendance = float(request.form['attendance'])
        internal_marks = float(request.form['internal_marks'])
        gpa = float(request.form['gpa'])
        backlogs = int(request.form['backlogs'])
        assignments = float(request.form['assignments'])
        sleep = float(request.form['sleep'])
        participation = int(request.form['participation'])
        score = 0
        reasons = []
        analysis = []
        suggestions = []

        # ---------- Scoring logic ----------
        if study_hours >= 4:
            score += 2
            reasons.append("Good daily study hours")
        elif study_hours >= 2:
            score += 1
            reasons.append("Average study hours")
        if attendance >= 75:
            score += 2
            reasons.append("Good attendance")
        elif attendance >= 60:
            score += 1
            reasons.append("Average attendance")
        if internal_marks >= 40:
            score += 2
            reasons.append("Good internal performance")
        elif internal_marks >= 30:
            score += 1
            reasons.append("Average internal marks")
        max_score = 20
        confidence = int((score / max_score) * 100)

        # ---------- Prediction ----------
        if confidence >= 75:
            prediction = "High Performance"
            reason = "Most academic and behavioral parameters are strong."
        elif confidence >= 50:
            prediction = "Medium Performance"
            reason = "Overall performance is balanced, but some parameters need improvement."
        else:
            prediction = "Needs Improvement"
            reason = "Multiple parameters require attention."
        
        suggestions = []

        if study_hours < 4:
            suggestions.append("Increase daily study hours to at least 4 hours")

        if attendance < 75:
            suggestions.append("Improve attendance above 75%")

        if gpa < 7:
            suggestions.append("Focus on improving GPA through regular revision")

        if assignments < 80:
            suggestions.append("Submit assignments on time with better quality")

        if sleep < 6:
            suggestions.append("Maintain healthy sleep of 6–8 hours daily")
  
        # ---------- Render ----------
        return render_template(
            'index.html',
            prediction=prediction,
            confidence=confidence,
            score=score,
            reasons=reasons,
            form_data=request.form,
            suggestions=suggestions
        )


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
