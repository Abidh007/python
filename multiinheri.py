class Student:
    def getData(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course

    def displayStudent(self):
        print("Roll No:",self.rollno)
        print("name of student:",self.name)
        print("course:",self.course)

#inheritance
class Test(Student):
    def getMarks(self,marks):
        self.marks=marks
    def displayMarks(self):
        print("Total marks:",self.marks)

class Sports:
    def getSportsMarks(self,spmarks):
        self.spmarks=spmarks
    def displaySportsMarks(self):
        print("Sports marks:",self.spmarks)
    

#multipel inheritance
class Result(Test,Sports):
    def calculateGrade(self):
        m=self.marks+self.spmarks
        if m>480:self.grade="Distinction"
        elif m>360: self.grade="First class"
        elif m>240: sel.grade="secon class"
        else: self.grade="failed"
        print("result:",self.grade)

#main program
r=int(input("Enter Roll Number:"))
n=input("Enter Name:")
c=input("Enter course Name:")
m=int(input("Enter Marks:"))
s=int(input("enter sports marks:"))

#creating of object
print("Result")
stud1=Result() #instance of child
stud1.getData(r,n,c)
stud1.getMarks(m)
stud1.getSportsMarks(s)
stud1.displayStudent()
stud1.displayMarks()
stud1.displaySportsMarks()
stud1.calculateGrade()
