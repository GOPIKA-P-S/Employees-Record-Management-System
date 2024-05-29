import mysql.connector

class Employee:
    name = ""
    age = 0
    salary = 0
    __conn = ""
    __cursor = "" 
    
    def _init_(self):
        Employee.connect()
    
    @staticmethod    
    def connect():
        global __conn
        global __cursor
        __conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="employee_management"
        )
        __cursor = __conn.cursor()

        # self.cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, salary DECIMAL(10, 2))")
        # self.conn.commit()
    
    @staticmethod
    def connectionclose():
        __conn.close()
        
    @staticmethod
    def display():
        Employee.connect()
        query = "SELECT * FROM employees"
        __cursor.execute(query)
        result = __cursor.fetchall()
        # if Employee is Empty
        if not result:
            print(f"No employees ")
            return
        for row in result:
            # print(row)
            print(f"Name : {row[0].ljust(15)} Age : {row[1]} Salary : {str(row[2]).ljust(10)}")
        Employee.connectionclose()

    def add(self):        
        query = "INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)"
        values = (self.name, self.age, self.salary)

        __cursor.execute(query, values)
        __conn.commit()        
        Employee.connectionclose()
    
    def is_employee_exists(self):
        check_query = "SELECT * FROM employees WHERE name = %s"
        check_values = (self.name,)

        __cursor.execute(check_query, check_values)
        result = __cursor.fetchall()

        return result
            # 
            # return
    def edit(self, edit_name):      

        # Check if the name exists before attempting to edit
        
        # If the name exists, proceed with the edit
        
        edit_query = "UPDATE employees SET name = %s, age = %s, salary = %s WHERE name = %s"
        edit_values = (self.name, self.age, self.salary, edit_name)

        __cursor.execute(edit_query, edit_values)
        __conn.commit()
        Employee.connectionclose()

    def delete(self):
       # If the name exists, proceed with the deletion
        delete_query = "DELETE FROM employees WHERE name = %s"
        delete_values = (self.name,)

        __cursor.execute(delete_query, delete_values)
        __conn.commit()
        Employee.connectionclose()
       
print("Employee Record Management System")
while True:
    print("====================================")
    print("Menu")
    print("Please select your input")
    print("1. List")
    print("2. Add")
    print("3. Edit")
    print("4. Delete")
    print("5. Exit")
    inp = int(input("Select your choice : "))

    if inp == 1:        
        Employee.display()
    elif inp == 2:
        employee = Employee()
        employee.name = input("Enter employee name: ")
        employee.age = int(input("Enter employee age: "))
        employee.salary = float(input("Enter employee salary: "))   
        employee.add()
        print("Employee added successfully!")
    elif inp == 3:
        employee = Employee()
        employee.name = input("Enter employee Name to edit: ")
        edit_name = employee.name
        if not employee.is_employee_exists():
            print(f"No employee found with the name '{employee.name}'. Edit aborted.")
        else:
            employee.name = input("Enter employee's new Name: ")
            employee.age = int(input("Enter new Age: "))
            employee.salary = float(input("Enter new Salary: "))
            employee.edit(edit_name)
            print("Employee information updated successfully!")
    elif inp == 4:
        employee = Employee()
        employee.name = input("Enter employee Name to delete: ")
        edit_name = employee.name
        if not employee.is_employee_exists():
            print(f"No employee found with the name '{employee.name}'. Delete aborted.")
        else:
            employee.delete()
            print("Employee deleted successfully!")
    elif inp == 5:
        exit()
    else:
        print("Invalid input. Please select a valid option.")