class Employee():
    all_ids = set()

    def __init__(self, ID, name, age, salary):
        self.ID = ID
        self.name = name
        self.age = age
        self.salary = salary

    def Emp_data(self):
        self.__employee_id = ()
        self.__employee_id = self.__employee_id + (self.ID,)
        self.__salary = []
        self.__salary.append(self.salary)
        self.stored_name = []
        self.stored_name.append(self.name)
        self.stored_age = []
        self.stored_age.append(self.age)

    def getter(self):
        return self.__employee_id, self.__salary

    def salary_setter(self, newSalary):
        self.__salary.append(newSalary)

    def emp_id_setter(self, newId):
        if newId in Employee.all_ids:
            print("This Employee ID already exists!")
            return
        else:
            self.__employee_id = self.__employee_id + (newId,)

    def display(self, ID):
        if ID == self.__employee_id[0]:
            print("Employee Details:")
            print(f"Name: {self.stored_name[0]}")
            print(f"Age: {self.stored_age[0]}")
            print(f"Employee ID: {self.__employee_id[0]}")
            print(f"Salary: ${self.__salary[0]}")
            return
        else:
            print("Employee ID not found!")

    def __del__(self):
        print("\nExiting the system. All resources have been freed.")        

class Manager(Employee):
    def __init__(self, ID, name, age, salary, dep):
        super().__init__(ID, name, age, salary)
        self.Emp_data()
        self.department = []
        self.department.append(dep)

    def display(self, ID):
        if ID == self.getter()[0][0]:
            print("Manager Details:")
            print(f"Name: {self.stored_name[0]}")
            print(f"Age: {self.stored_age[0]}")
            print(f"Manager ID: {self.getter()[0][0]}")
            print(f"Salary: ${self.getter()[1][0]}")
            print(f"Department: {self.department[0]}")
            return
        else:
            print("Manager ID not found!")


class Developer(Employee):
    def __init__(self, ID, name, age, salary, languages):
        super().__init__(ID, name, age, salary)
        self.Emp_data()
        self.languages = []
        lans = set(languages.split(","))
        self.languages.append(lans)

    def display(self, ID):
        if ID == self.getter()[0][0]:
            print("\nDeveloper Details:")
            print(f"Name: {self.stored_name[0]}")
            print(f"Age: {self.stored_age[0]}")
            print(f"Developer ID: {self.getter()[0][0]}")
            print(f"Salary: ${self.getter()[1][0]}")
            print(f"Languages: {self.languages[0]}")
            return
        else:
            print("Developer ID not found!")

run = 0

devs = []
emps = []
mans = []

print("--- Python OOP Project: Employee Management System ---")

while True:
    run += 1
    if run > 1:
        print("\n--- Choose another operation ---")

    print("\nChoose an operation:")
    print("1. Create a Developer")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    match choice:
        case "1":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            eID = input("Enter Developer ID: ")
            salary = int(input("Enter Salary: "))
            languages = input("Enter Languages(Comma-separated): ")

            if eID in Employee.all_ids:
                print("\nThis Employee ID already exists!")
            else:
                dev = Developer(eID, name, age, salary, languages)
                Employee.all_ids.add(eID)
                devs.append(dev)
                print("\nDeveloper created successfully!")

        case "2":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            eID = input("Enter Employee ID: ")
            salary = int(input("Enter Salary: "))

            if eID in Employee.all_ids:
                print("\nThis Employee ID already exists!")
            else:
                emp = Employee(eID, name, age, salary)
                emp.Emp_data()
                Employee.all_ids.add(eID)
                emps.append(emp)
                print("\nEmployee created successfully!")

        case "3":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            eID = input("Enter Manager ID: ")
            salary = int(input("Enter Salary: "))
            dept = input("Enter Department: ")

            if eID in Employee.all_ids:
                print("\nThis Employee ID already exists!")
            else:
                man = Manager(eID, name, age, salary, dept)
                Employee.all_ids.add(eID)
                mans.append(man)
                print("\nManager created successfully!")

        case "4":
            print("\nChoose details to show:")
            print("1. Developer")
            print("2. Employee")
            print("3. Manager")

            opt = input("Enter your choice: ")

            match opt:
                case "1":
                    show_id = input("Enter Developer ID to check: ")
                    found = False
                    for dev in devs:
                        if show_id == dev.getter()[0][0]:
                            dev.display(show_id)
                            found = True
                            break
                        else:
                            continue

                    if found == False:
                        print("Developer ID not found!")

                case "2":
                    show_id = input("Enter Employee ID to check: ")
                    found = False
                    for emp in emps:
                        if show_id == emp.getter()[0][0]:
                            emp.display(show_id)
                            found = True
                            break
                        else:
                            continue

                    if found == False:
                        print("Employee ID not found!")

                case "3":
                    show_id = input("Enter Manager ID to check: ")
                    found = False
                    for man in mans:
                        if show_id == man.getter()[0][0]:
                            man.display(show_id)
                            found = True
                            break
                        else:
                            continue

                    if found == False:
                        print("Manager ID not found!")

        case "5":
            del devs
            del emps
            del mans
            break
print("\nGoodbye!")