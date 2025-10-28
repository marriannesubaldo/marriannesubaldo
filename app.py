from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my Flask API!",
        "status": "success"
    }), 200


# GET: Retrieve student data
@app.route('/student', methods=['GET'])
def get_student():
    student = {
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    }
    return jsonify(student), 200


# POST: Add new student data (example)
@app.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    
    # Basic validation
    if not data or 'name' not in data or 'grade' not in data or 'section' not in data:
        return jsonify({
            "error": "Invalid input. Please provide name, grade, and section."
        }), 400

    return jsonify({
        "message": "Student added successfully!",
        "student": data
    }), 201


# Handle 404 errors gracefully
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Resource not found"
    }), 404


if __name__ == '__main__':
    app.run(debug=True)
