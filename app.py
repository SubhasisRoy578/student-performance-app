from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = 0
    score = 0
    reasons = []
    suggestions = []
    form_data = {}

    if request.method == "POST":
        # Read form data
        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        internal_marks = float(request.form["internal_marks"])
        gpa = float(request.form["gpa"])
        backlogs = int(request.form["backlogs"])
        assignments = float(request.form["assignments"])
        sleep = float(request.form["sleep"])
        participation = int(request.form["participation"])

        # Store values to keep inputs after submit
        form_data = request.form

        # Simple scoring logic
        score = 0
        if study_hours >= 4: score += 2
        if attendance >= 75: score += 2
        if internal_marks >= 60: score += 2
        if gpa >= 7: score += 2
        if backlogs == 0: score += 2
        if assignments >= 70: score += 1
        if sleep >= 7: score += 1
        if participation == 2: score += 1

        # Prediction
        if score >= 10:
            prediction = "High Performance"
            confidence = 85
        elif score >= 6:
            prediction = "Medium Performance"
            confidence = 65
        else:
            prediction = "Low Performance"
            confidence = 40

        # Reasons
        if attendance >= 75:
            reasons.append("Good attendance")
        if internal_marks >= 60:
            reasons.append("Good internal performance")
        if study_hours >= 4:
            reasons.append("Sufficient study hours")
        if gpa >= 7:
            reasons.append("Strong previous GPA")

        # Suggestions (IMPROVED LOGIC)
        if attendance < 75:
            suggestions.append("Improve attendance to at least 75%")
        if study_hours < 4:
            suggestions.append("Increase daily study hours")
        if internal_marks < 60:
            suggestions.append("Focus on internal assessments")
        if assignments < 70:
            suggestions.append("Submit assignments on time")
        if sleep < 7:
            suggestions.append("Maintain proper sleep schedule")
        if backlogs > 0:
            suggestions.append("Clear backlogs as early as possible")

        if not suggestions:
            suggestions.append("Keep maintaining your current performance")

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        score=score,
        reasons=reasons,
        suggestions=suggestions,
        form_data=form_data
    )

if __name__ == "__main__":
    app.run(debug=True)


