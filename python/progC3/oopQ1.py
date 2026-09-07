class Student:
    def __init__(self, name, student_number, mark):
        self.name = name
        self.student_number = student_number
        self.mark = mark
        
        # Calculate result based on mark
        if mark > 50:
            self.result = "pass"
        else:
            self.result = "failed"
    
    def display_details(self):
        print(f"Student: {self.name} \nNumber: {self.student_number} \n")
    
    def display_result(self):
        print(f"\nStudent: {self.name} \nNumber: {self.student_number} \nMarks: {self.mark} \nStatus: {self.result}")

# Create student - only 3 args now ✅
s1 = Student("Thabo", "060111",67)
s2 = Student("charles","07112",78)
s3 = Student("kevin","01234",40)
s1.display_details()
s2.display_result()
s3.display_result()