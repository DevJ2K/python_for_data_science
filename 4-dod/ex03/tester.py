from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)

try:
    student = Student(name="Edward", surname="agle", id="toto")
except Exception as e:
    print(f"{type(e).__name__}: {str(e)}")
