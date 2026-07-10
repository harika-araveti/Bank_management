class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print("your average marks is ",sum/4)
s1 = Student("harika",[92,93,94,95])
s1.average()    