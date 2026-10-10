from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

students = []
attendance = []

@app.route("/")
def home():
    return render_template("index.html", students=students)

@app.route("/register"@app.route("/mark_attendance/<int:student_index>", methods=["POST"])
def mark_attendance(student_index):
    student = students[student_index]

    record = {
        "name": student["name"],
        "roll_number": student["roll_number"],
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "status": "Present"
    }

    attendance.append(record)

    return render_template(
        "index.html",
        students=students,
        attendance=attendance
    ), methods=["POST"])
def register():
    name = request.form["name"]
    roll_number = request.form["roll_number"]

    student = {
        "name": name,
        "roll_number": roll_number
    }

    students.append(student)

    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
