import csv


class Course:
    name = ''
    line = []
    def __init__(self, name):
        self.name = name
        with open('course.csv','r') as course:
            value = csv.reader(course)
            for row in value:
                if row[0] == name:
                    self.line = row[1:]

    def get_course_details(self):
        v = self.line
        if len(v) != 0:
            print("***************************************************")
            print(f"Available course of study for the course {self.name}\n")
            print("***************************************************")
            for row in self.line:
                print(f"-{row}")
        else:
            print("Currently no available\n")

    def check_availability(self):
        c = self.line
        print(len(c))
        if len(c) == 0:
            return False
        return True


class Student:
    name = ''
    id = ''
    course = ''
    bal = ''
    due = ''
    data = []

    def __init__(self, name=None, id=None, course=None):
        with open('student.csv', 'r') as student:
            d = csv.DictReader(student, ['Name', 'id', 'course', 'bal', 'due'])
            self.data = list(d)
            self.name = name
            self.id = id
            self.course = course
        if name == None and id == None and course == None:
            print("Students details:\n")
            return
        for d in self.data:
            if d["Name"] == name and d["id"] == id and d["course"] == course:
                self.bal = d['bal']
                self.due = d['due']
                self.data.remove(d)
                return
        
        print("Invalid details ,please check these info\n")

    def get_details(self, name, id, course):
        with open('student.csv', 'r') as student:
            d = csv.DictReader(student, ['Name', 'id', 'course', 'bal', 'due'])
            for info in list(d):
                if info["Name"] == name and info["id"] == id and info["course"] == course:
                    print("***********************\n")
                    print(f"Name: {info['Name']}")
                    print(f"id: {info['id']}")
                    print(f"course: {info['course']}")
                    print(f"Balance: {info['bal']}")
                    print(f"Due: {info['due']}")
                    print("***********************")
                    return
        print("Sorry, no info available\n")
        return

    def enroll(self):
        d = self.data
        for info in d:
            if info["Name"] == self.name and info["course"] == self.course:
                print("Sorry, you are already in the course\n")
                return

        self.id = len(d)+1
        self.due = 20000
        self.pay()
        return

    def pay(self):
        v = self.due
        if len(v) != 0:
            if int(self.due) == 20000:
                opt = input("You have two installments to pay press 1 to pay all or 2 to pay first installment\n")
                if int(opt) == 1:
                    self.due = 0
                    self.bal = 20000
                elif int(opt) == 2:
                    self.due = 10000
                    self.bal = 10000
                else:
                    print("Error choice\n")
                    self.pay()
                print("You are successfully registered\n")

            elif int(self.due) == 10000:
                opt = input("Please press 1 to pay the remaining installment\n")
                if int(opt) == 1:
                    self.bal = 20000
                    self.due = 0
            else:
                print("You have already paid full\n")
            print("*******************")
            print("You current status")
            print("Name:", self.name)
            print("Course:", self.course)
            print("Id:", self.id)
            print("Balance:", self.bal)
            print("Due:", self.due)
            print("*******************")
            self.update()
        return

    def get_student_detail(self):
        with open('student.csv', 'r') as student:
            data = csv.DictReader(student)
            for i in list(data):
                print("*********************")
                print("Name:", i['Name'])
                print("Course:", i['course'])
                print("Id:", i['id'])
                print("Balance:", i['bal'])
                print("Due:", i['due'])
                print("*********************")

    def returnDeposit(self):
        if self.due == '20000':
            self.due = 20000
            self.bal = 0
            self.update()
            print("Succesfully Returned deposit\n")
        else:
            print("Complete the course first\n")

    def update(self, name=None):
        with open('student.csv', 'w') as student:
            save = csv.DictWriter(student, ["Name", 'id', 'course', 'bal', 'due'])
            if name == None :
                self.data += [{"Name": self.name, "id": self.id, "course": self.course, "bal": self.bal, "due": self.due}]
                save.writerows(self.data)
            else:
                self.data += [{"Name": name, "id": self.id, "course": self.course, "bal": self.bal, "due": self.due}]
                save.writerows(self.data)
                
        return

    def delete(self):
        with open('student.csv', 'w') as student:
            save = csv.DictWriter(student, ["Name", 'id', 'course', 'bal', 'due'])
            save.writerows(self.data)


print("Welcome to our console app.\n")
Repeat = True
while Repeat:
    try:
        o = int(input("Enter 1 to see Menu\n"))
    except ValueError:
        print("Enter integer\n")
    if o == 1:
        opt = input("Enter the One of the available option\n"
                    "1.Get Course Details\n"
                    "2.Get Student details\n"
                    "3.Enroll into course\n"
                    "4.Pay \n"
                    "5.Get all details\n"
                    "6.Delete Student\n"
                    "7.Update student\n"
                    "8.Return Deposit\n"
                    "9.Exit\n"
                    )
        option = int(opt)
        if option == 9:
            Repeat = False
        if option == 1:
            name = input("Enter Course Name\n")
            c = Course(name)
            c.get_course_details()
        if option == 2:
            name = input("Enter student name\n")
            id = input("Enter id\n")
            course = input("Enter course name\n")
            s = Student(name, id, course)
            s.get_details(name, id, course)
        if option == 3:
            name = input("Enter student name\n")
            course = input("Enter course name\n")
            c = Course(course)
            print("Checking availability ....\n")

            if c.check_availability():
                s = Student(name, id, course)
                s.enroll()
            print("No course available of that name\n")
        if option == 4:
            name = input("Enter student name\n")
            id = input("Enter id\n")
            course = input("Enter course name\n")
            s = Student(name, id, course)
            s.pay()
        if option == 5:
            s = Student()
            s.get_student_detail()
        if option == 6:
            name = input("Enter student name\n")
            id = input("Enter id\n")
            course = input("Enter course name\n")
            s = Student(name, id, course)
            s.delete()
        if option == 7:
            name = input("Enter student name\n")
            id = input("Enter id\n")
            course = input("Enter course name\n")
            name2 = input("Enter name to update")
            s = Student(name, id, course)
            s.update(name2)
        if option == 8:
            name = input("Enter student name\n")
            id = input("Enter id\n")
            course = input("Enter course name\n")
            s = Student(name, id, course)
            s.returnDeposit()
            





print("Exiting.....")
