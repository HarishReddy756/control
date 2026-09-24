age=20
if age>=10:
    print("you are eligible for vote")

age=13
if age>=18:
    print("eligible to vote")
else:
    print("not eligible for vote")

marks=83
if marks>=90:
    grade="A+"
elif marks>=85:
    grade="A"
elif marks>=79:
    grade="B"
elif marks>=60:
    grade="C"
elif marks>=40:
    grade="F"
else:
    grade="fail"
print("Grade:",grade)
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
students=["mastan,ashok,harish,siva"]
for student in students:
    print(student)

print("Hello")
for i in range(1,3):
    for j in range(1,10):
        print(i*j,end=" ")
print()
for i in range(2,5):
    print(i)

students={
	"amit":[80,70,49],
	"Priya":[85,94,83],
	"harish":[84,93,92]
}
for name,marks in students.items():
    total=0
    for mark in marks:
     total+= mark
    print(name,"Total:",total)

for i in range(1,19):
    if(i==7):
        break
    print(i)

for i in range(0,8):
    if(i==7):
        continue
    print(i)

for i in range(7,10):
    if(i==8):
        pass
    print(i)

name="Harish Reddy"
print(name[0])
print(name[6])
print(name[7])
print(name[-6])
print(name[0:4])
print(name[-4:-9])


students = [
    ["Rahul",85],
    ["Priya",90],
    ["Amit",78]
    ]
print(students)
print(students[0])
print(students[0][0])
print(students[0][1])
students[1][1] = 95
print(students)

employees = [
    ["E101", "Rahul", "Developer", 50000],
    ["E102", "Priya", "Tester", 45000],
    ["E103", "Amit", "Manager", 70000]
]
 
# Display first employee
print(employees[0])
print(employees[0][1])
employees[0][3] = 55
print(employees[1][1])
print(employees[2][3])
print(employees[0][1])
employees[0][3] = 55000
print(employees[0])
employees.append(
    ["E104", "Sneha", "Developer", 60000]
)
print(employees)
employees.remove(
    ["E102", "Priya", "Tester", 45000]
)
print(employees)

numbers = (10, 20, 30, 40, 50)
 
print(numbers[1:4])
 
print(numbers[:3])

print(numbers[2:])

print(numbers[::-1])


a=2
tuple_a=("eight",4,9.3,a)
print(type(tuple_a))
print(tuple_a)

python_students={"harish","hari","karthik","balu"}
java_students={"hari","rajesh","swathi","harish"}
print("all students:")
print(python_students|java_students)

print("\n students who know both:")
print(python_students&java_students)

print("\n only python_students")
print(python_students-java_students)

print("\n only java_students")
print(python_students- java_students)

print("\nstudents who know the only one language:")
print(python_students^java_students)

student={"name":"harish","age":39,"course":"python","marks":91}
print(student)
student={}
print=(student)
student["name"]="rahul"
student["age"]=39



student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}
 
 
student["city"] = "Pune"
 
student.update({
    "age": 24,
    "city": "Mumbai",
    "course": "Data Science"
 
})
print(student["name"])

student = {

    "name": "Rahul",
    "age": 22,
    "course": "Python"

}
print(student.keys())
