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
r=int(input("Enter Roll Number:"))
n=input("Enter Name:")
c=input("Enter course Name:")
m=int(input("Enter Marks:"))

#creating of object
print("Result")
stud1=Test() #instance o child
stud1.getData(r,n,c)
stud1.getMarks(m)
stud1.displayStudent()
stud1.displayMarks()
