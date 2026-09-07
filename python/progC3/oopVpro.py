#Procedural style:
name = " thabo"
mark = 72

def print_result(name , result) :
    print(f"name : {name} \n score : {result}")
    
print_result(name, mark)

#OOP style

class Class:
    def __init__(self, student):
        self.student = student
        self.score = 0

    def add_score(self, score):
        self.score = score


student = Class("Tommy")

student.add_score(500)

print(student.student)
print(student.score)