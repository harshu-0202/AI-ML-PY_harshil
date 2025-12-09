class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("\n--- Person Details ---")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print("\n--- Employee Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        print("\n--- Manager Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Department:", self.department)


# Storage
persons = []
employees = []
managers = []

# Menu Loop
while True:
    print("\n--- Python OOP Project: Employee Management System ---\n")
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        person = Person(name, age)
        persons.append(person)
        print("Person created successfully!")

    elif choice == 2:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        emp = Employee(name, age, emp_id, salary)
        employees.append(emp)
        print("Employee created successfully!")

    elif choice == 3:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        department = input("Enter department: ")
        mgr = Manager(name, age, emp_id, salary, department)
        managers.append(mgr)
        print("Manager created successfully!")

    elif choice == 4:
        print("\n--- Showing All Saved Details ---")

        if not persons and not employees and not managers:
            print("No data available!")
        else:
            for p in persons:
                p.show_details()
            for e in employees:
                e.show_details()
            for m in managers:
                m.show_details()

    elif choice == 5:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
