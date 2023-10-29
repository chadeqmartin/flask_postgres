from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# init Flask
app = Flask(__name__)

#reference config to the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chadmartin@localhost/students'

#init sqlalchemy
db = SQLAlchemy(app)


#turned data table that Python program can talk to
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

#pulls/selects all data from the table student
with app.app_context():
    students = Student.query.all()

@app.route('/students/', methods=['GET'])
def get_students():
    students_list = []
    for student in students:
        students_list.append({'id': student.id, 
                              'first_name': student.first_name,
                              'last_name': student.last_name,
                              'age': student.age,
                              'grade': student.grade})
    return jsonify(students_list)

@app.route('/old_students/', methods = ['GET'])
def get_old_students():
    old_students = [student for student in students if student.age > 20]
    return jsonify(old_students)

@app.route('/young_students/', methods=['GET'])
def get_young_students():
    young_students = [student for student in students if student.age < 21]
    return jsonify(young_students)

@app.route('/advance_students/', methods=['GET'])
def get_advanced_students():
    advanceds_students = [student for student in students if student.age < 21 and student.grade == 'A']
    return jsonify(advanceds_students)

@app.route('/student_names/', methods = ['GET'])
def get_student_names():
    student_names = [{'first_name': student.first_name, 
                      'last_name': student.last_name} 
                      for student in students]
    return jsonify(student_names)

@app.route('/student_ages/', methods = ['GET'])
def get_student_ages():
    student_ages =[{'student_name': student.first_name + ' ' + student.last_name, 
                    'age': student.age} 
                    for student in students] 
    return jsonify(student_ages)

app.run(debug=True)