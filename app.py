from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        score = 0
        reasons = []
        gpa = float(request.form['gpa'])
        backlogs = int(request.form['backlogs'])
        assignments = float(request.form['assignments'])
        sleep = float(request.form['sleep'])
        participation = int(request.form['participation'])

        # Example inputs (make sure these exist above)
        # gpa, backlogs, assignments, sleep, participation

        if gpa >= 7:
            score += 2
            reasons.append("Good GPA")
        elif gpa >= 6:
            score += 1
            reasons.append("Average GPA")

        if backlogs == 0:
            score += 2
            reasons.append("No backlogs")
        elif backlogs == 1:
            score += 1
            reasons.append("One backlog")

        if assignments >= 80:
            score += 2
            reasons.append("Excellent assignments")
        elif assignments >= 60:
            score += 1
            reasons.append("Average assignments")

        if sleep >= 6:
            score += 1
            reasons.append("Healthy sleep")

        score += participation
        max_score = 14
        confidence = int((score / max_score) * 100)

        if confidence >= 75:
            prediction = "High Performance"
        elif confidence >= 50:
            prediction = "Medium Performance"
        else:
            prediction = "Needs Improvement"

        return render_template(
            'index.html',
            prediction=prediction,
            confidence=confidence,
            score=score,
            reasons=reasons
        )
    return render_template('index.html')
if __name__ == '__main__':
    app.run()

