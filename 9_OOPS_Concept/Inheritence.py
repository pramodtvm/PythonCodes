

class myclass():
    def __init__(self,x):
        self.x = x
        print("Initializing Variable")

    def add(self,a,b):
        print("Printing X",self.x)
        return a + b

    def subs(self,a,b):
        return a - b

class subclass(myclass):
    def __init__(self,last):
        self.last = last
        #self.x = x
        #print(self.last)
        #print(last)

#inst = subclass("raveendran")
#print(inst.last)
#print(inst.x)

class User:
    name = ""
    def __init__(self, name):
        self.name = name
        print("Inside parent Init  = " + self.name)

    def printName(self):
        print("Inside Name  = " + self.name)

class Programmer(User):
    def __init__(self, name):
        self.name = name
        print("inside init programmer",self.name)

    def doPython(self):
        print("Programming Python")



#brian = User("brian")
#brian.printName()

#diana = Programmer("Diana")
#diana.printName()
#diana.doPython()


# Line:1, definition of the superclass starts here
class Person:
    # initializing the variables
    name = "dude"
    age = 0
    # defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
        print("ParentClass INIT Prints", self.name)
        # defining class methods
    def showName(self):
        print("Show Name Func",self.name)

    def showAge(self):
        print("show age func",self.age)
        # Line: 19, end of superclass definition

# definition of subclass starts here
class Student(Person):  # Line: 22, Person is the  superclass and Student is the subclass
    studentId = ""
    def __init__(self, studentName, studentAge, studentId):
        Person.__init__(self, studentName,studentAge)  # Line: 26, Calling the superclass constructor and sending values of attributes.
        self.studentId = studentId
        print("Printing in subclas INIT",self.studentId)

    def getId(self):
        return self.studentId  # returns the value of student id


# end of subclass definition
# Create an object of the superclass
#person1 = Person("Richard", 23)  # Line: 35
# call member methods of the objects
#person1.showAge()
# Create an object of the subclass
#student1 = Student("Max", 22, "102")  # Line: 39
#print(student1.getId())
#student1.showName()  # Line: 41


class Person123:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student123(Person123):
    #   Class Constructor
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    # Write your constructor here
    def __init__(self,firstName,lastName,ids,scores):
        self.firstName =firstName
        self.lastName =lastName
        print("numsc",self.firstName)
        #print("numsc",last)
        print("numsc",ids)
        print("numsc",scores)

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        pass



line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student123(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())