from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://annascriven@localhost/students"

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

    def __repr__(self):
        return self.first_name
    
@app.route("/students/", methods = ['GET'])
def get_students():
    students = Student.query.all()  
    print(type(students))
    formatted_students= []
    for stud in students:
            formatted_students.append({ "id":stud.id,
             "first_name":stud.first_name,
             "last_name":stud.last_name,
             "age":stud.age,
             "grade":stud.grade
                 })  

    return jsonify(formatted_students)

@app.route("/old_students/", methods = ['GET'])
def get_old_students():
    old_students = Student.query.filter(Student.age>20)
    formatted_students= []
    for stud in old_students:
            formatted_students.append({ "id":stud.id,
             "first_name":stud.first_name,
             "last_name":stud.last_name,
             "age":stud.age,
             "grade":stud.grade
                 })  
          
    return jsonify(formatted_students)

@app.route("/advance_students/", methods = ['GET'])
def get_advanced_students():
    advanced_students = Student.query.filter(Student.age<21, Student.grade =='A')
    formatted_students = []
    for stud in advanced_students:
        formatted_students.append({ "id":stud.id,
             "first_name":stud.first_name,
             "last_name":stud.last_name,
             "age":stud.age,
             "grade":stud.grade
                 })  
    return jsonify(formatted_students)

@app.route("/student_names/", methods = ['GET'])
def get_student_names():
    names=Student.query.all()
    formatted_students = []
    for stud in names:
        formatted_students.append({ 
             "first_name":stud.first_name,
             "last_name":stud.last_name,
                 })  
    return jsonify(formatted_students)

@app.route("/student_ages/", methods= ['GET'])
def get_student_ages():
    students = Student.query.all()
    formatted_students = []
    for stud in students:
        formatted_students.append({ "id":stud.id,
            "name":stud.first_name+stud.last_name,
             "age":stud.age,
                 })  
    return jsonify(formatted_students)

@app.route("/young_students/", methods=['GET'])
def get_young_students():
    young_students = Student.query.filter(Student.age<21)
    formatted_students = []
    for stud in young_students:
        formatted_students.append({ "id":stud.id,
             "name":stud.first_name+stud.last_name,
             "age":stud.age,
                 })  
    return jsonify(formatted_students)



app.run(debug = True)