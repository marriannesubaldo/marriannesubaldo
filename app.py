from flask import Flask, jsonify, request, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# -----------------------
# In-Memory Data Storage
# -----------------------
students = [
    {"id": 1, "name": "John Doe", "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "Jane Smith", "grade": 11, "section": "Ezekiel"}
]

# -----------------------
# Web Design Route
# -----------------------
@app.route('/')
def home():
    """Render a simple HTML homepage with styling."""
    return render_template('index.html', title="My Flask API")


# -----------------------
# API ROUTES
# -----------------------

@app.route('/api/students', methods=['GET'])
def get_students():
    """Return all students."""
    return jsonify({
        "status": "success",
        "count": len(students),
        "students": students
    }), 200


@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get a single student by ID."""
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404


@app.route('/api/students', methods=['POST'])
def add_student():
    """Add a new student."""
    data = request.get_json()
    if not data or 'name' not in data or 'grade' not in data or 'section' not in data:
        return jsonify({"error": "Invalid input. Provide name, grade, and section."}), 400

    new_student = {
        "id": len(students) + 1,
        "name": data['name'],
        "grade": data['grade'],
        "section": data['section'],
        "created_at": datetime.utcnow().isoformat()
    }
    students.append(new_student)

    return jsonify({
        "message": "Student added successfully!",
        "student": new_student
    }), 201


@app.errorhandler(404)
def not_found(error):
    """Custom 404 handler."""
    return jsonify({"error": "Resource not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
