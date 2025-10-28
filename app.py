from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# -----------------------
# In-memory "database"
# -----------------------
students = [
    {"id": 1, "name": "John Doe", "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "Jane Smith", "grade": 11, "section": "Ezekiel"}
]

# -----------------------
# HOME PAGE (with HTML design)
# -----------------------
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My Flask Student API</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(to right, #74ebd5, #ACB6E5);
                color: #333;
                text-align: center;
                margin: 0;
                padding: 0;
            }

            header {
                background-color: rgba(0, 0, 0, 0.2);
                padding: 1.5rem;
                color: white;
                font-size: 1.5rem;
                font-weight: bold;
            }

            main {
                margin-top: 60px;
            }

            .button {
                background-color: #4CAF50;
                color: white;
                padding: 12px 24px;
                text-decoration: none;
                border-radius: 6px;
                font-weight: bold;
                transition: 0.3s;
            }

            .button:hover {
                background-color: #45a049;
            }

            footer {
                margin-top: 50px;
                padding: 1rem;
                font-size: 0.9rem;
                color: #555;
            }

            .api-info {
                background: rgba(255, 255, 255, 0.7);
                padding: 20px;
                margin: 20px auto;
                width: 50%;
                border-radius: 10px;
            }

            ul {
                list-style-type: none;
                padding: 0;
            }

            li {
                margin: 8px 0;
            }
        </style>
    </head>
    <body>
        <header>🌐 Welcome to My Flask Student API</header>

        <main>
            <div class="api-info">
                <h2>📘 Flask + JSON API Demo</h2>
                <p>This API manages student information dynamically.</p>

                <h3>Available Endpoints:</h3>
                <ul>
                    <li>GET → <code>/api/students</code> – List all students</li>
                    <li>GET → <code>/api/students/&lt;id&gt;</code> – Get one student</li>
                    <li>POST → <code>/api/students</code> – Add new student (JSON body)</li>
                </ul>

                <a href="/api/students" class="button">View All Students (JSON)</a>
            </div>
        </main>

        <footer>
            <p>Created with ❤️ using Flask | 2025</p>
        </footer>
    </body>
    </html>
    """
    return html_content


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
    """Return a single student by ID."""
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404


@app.route('/api/students', methods=['POST'])
def add_student():
    """Add a new student record."""
    data = request.get_json()
    
    # Basic validation
    if not data or 'name' not in data or 'grade' not in data or 'section' not in data:
        return jsonify({"error": "Invalid input. Please provide name, grade, and section."}), 400

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


# -----------------------
# ERROR HANDLERS
# -----------------------

@app.errorhandler(404)
def not_found(error):
    """Custom 404 error response."""
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error response."""
    return jsonify({"error": "Internal Server Error"}), 500


# -----------------------
# MAIN ENTRY POINT
# -----------------------
if __name__ == '__main__':
    app.run(debug=True)
