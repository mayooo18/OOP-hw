from employee import Employee

DATA_FILE = "employee_directory.dat"

def load_employees():
    employees = {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(",")
                if len(parts) != 4:
                    continue
                emp_id, name, dept, title = parts
                employees[emp_id] = Employee(emp_id, name, dept, title)
    except FileNotFoundError:
        pass
    return employees

def save_employees(employees):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write("# employee_id,name,department,title\n")
        for emp_id, emp in employees.items():
            f.write(f"{emp.get_employee_id()},{emp.get_name()},{emp.get_department()},{emp.get_title()}\n")

def main():
    employees = load_employees()
    while True:
        print("\nMenu")
        print("----------------------------------------")
        print("1. Look up an employee")
        print("2. Add a new employee")
        print("3. Change an existing employee")
        print("4. Delete an employee")
        print("5. Quit the program")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            emp_id = input("Enter an employee ID number: ")
            if emp_id in employees:
                print(employees[emp_id])
            else:
                print("The specified ID number was not found.")
        elif choice == "2":
            emp_id = input("Enter employee ID number: ")
            name = input("Enter employee name: ")
            dept = input("Enter employee department: ")
            title = input("Enter employee title: ")
            employees[emp_id] = Employee(emp_id, name, dept, title)
            print("The new employee has been added.")
        elif choice == "3":
            emp_id = input("Enter an employee ID number: ")
            if emp_id in employees:
                name = input("Enter the new name: ")
                dept = input("Enter the new department: ")
                title = input("Enter the new title: ")
                employees[emp_id].set_name(name)
                employees[emp_id].set_department(dept)
                employees[emp_id].set_title(title)
                print("Employee information updated.")
            else:
                print("The specified ID number was not found.")
        elif choice == "4":
            emp_id = input("Enter an employee ID number: ")
            if emp_id in employees:
                del employees[emp_id]
                print("Employee information deleted.")
            else:
                print("The ID number was not found.")
        elif choice == "5":
            save_employees(employees)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
