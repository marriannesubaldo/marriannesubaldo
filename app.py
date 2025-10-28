from flask import Flask, request, redirect, jsonify
from datetime import datetime

app = Flask(__name__)

# -----------------------
# In-memory "database"
# -----------------------
students = [
    {"id": 1, "name": "John Doe", "year": "1st Year", "section": "Zechariah"},
    {"id": 2, "name": "Jane Smith", "year": "2nd Year", "section": "Ezekiel"}
]


# -----------------------
# HOME PAGE (View + Add)
# -----------------------
@app.route('/')
def home():
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Student Management</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(to right, #74ebd5, #ACB6E5);
                margin: 0;
                padding: 0;
                color: #333;
            }}

            header {{
                background-color: #4a90e2;
                color: white;
                padding: 1.5rem;
                text-align: center;
                font-size: 1.8rem;
                font-weight: bold;
                letter-spacing: 1px;
            }}

            main {{
                max-width: 800px;
                margin: 30px auto;
                background: rgba(255, 255, 255, 0.95);
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}

            h2 {{
                color: #2c3e50;
            }}

            form {{
                margin-bottom: 30px;
            }}

            input[type="text"] {{
                padding: 10px;
                width: 90%;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }}

            button {{
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-weight: bold;
                transition: 0.3s;
            }}

            button:hover {{
                background-color: #45a049;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: center;
            }}

            th {{
                background-color: #4a90e2;
                color: white;
            }}

            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}

            footer {{
                text-align: center;
                padding: 15px;
                color: #555;
                margin-top: 40px;
            }}
        </style>
    </head>
    <body>
        <header>🎓 Student Management System</header>

        <main>
            <h2>Add a New Student</h2>
            <form action="/add" method="POST">
                <input type="text" name="name" placeholder="Full Name" required><br>
                <input type="text" name="year" placeholder="Year (e.g., 1st Year)" required><br>
                <input type="text" name="section" placeholder="Section" required><br>
                <button type="submit">Add Student</button>
            </form>

            <h2>All Students</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Year</th>
                    <th>Section</th>
                    <th>Added</th>
                </tr>
    """

    for s in students:
        html += f"""
                <tr>
                    <td>{s['id']}</td>
                    <td>{s['name']}</td>
                    <td>{s['year']}</td>
                    <td>{s['section']}</td>
                    <td>{s.get('created_at', '—')}</td>
                </tr>
        """

    html += """
            </table>
        </main>

        <footer>
            <p>Created with ❤️ using Flask | 2025</p>
        </footer>
    </body>
    </html>
    """
    return html


# -----------------------
# ADD STUDENT ROUTE
# -----------------------
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    year = request.form.get('year')
    section = request.form.get('section')

    if not name or not year or not section:
        return "Invalid input. Please fill all fields.", 400

    new_student = {
        "id": len(students) + 1,
        "name": name,
        "year": year,
        "section": section,
        "created_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }
    students.append(new_student)
    return redirect('/')


# -----------------------
# JSON API ROUTE (Optional)
# -----------------------
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students), 200


# -----------------------
# MAIN ENTRY POINT
# -----------------------
if __name__ == '__main__':
    app.run(debug=True)
