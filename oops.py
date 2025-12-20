# Object Oriented Programming


class Employee:
    number_of_employees = 0
    raise_amount = 1.04
    
    def __init__(self,name,age,department,salary):
        self.name = name
        self.age = age
        self.department = department
        self.email = self.name.replace(" ", ".").lower() + "@company.com"
        self.salary = salary
        
        Employee.number_of_employees += 1
        
    def employee_intro(self):
        return f"{self.name} works at the {self.department} department"
    
    def pay_raise(self):
        self.salary = self.salary * self.raise_amount
        
        
    # class method
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
        
    @classmethod
    def str_to_employee(cls,emp_str):
        first,last,age,department,salary = emp_str.split("-")
        full_name = first + " " + last
        return cls(full_name,age,department,salary)
        
        
        
employee1 = Employee("Arpit Mishra",25,"Engineering",50000)
print(employee1.name)
print(employee1.email)
print(employee1.employee_intro())

print(f"Number Of Employees In The Organization: {Employee.number_of_employees}")
print(f"********** Salary before pay raise ************")
print(employee1.salary)
employee1.pay_raise()
print(f"********** Salary after pay raise **************")
print(employee1.salary)


Employee.set_raise_amount(2)


emp_strs = ["Arpit-Mishra-25-Engineering-25000","Priyanshu-Jangid-27-Engineering-45000"]

new_employees = []
for index,emp in enumerate(emp_strs):
    new_employees.append(Employee.str_to_employee(emp))
    
    
print(new_employees[0].name)
print(new_employees[1].name)
    




