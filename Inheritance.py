class Employee:
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        
    def fullname(self):
        return f"Employee Name: {self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount
        

class Developer(Employee):
    raise_amount = 1.05
    
    def __init__(self, first, last, pay,role):
        super().__init__(first, last, pay)
        self.role = role
        
class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
            
        else:
            self.employees = employees
            
    def add_employees(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_employees(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
            
    def print_employees(self):
        for emp in self.employees:
            print('--->',emp.fullname())
        
        
dev1 = Developer("Arpit","Mishra",25000,"Backend Engineer")
dev2 = Developer("Priyanshu","Jangid",35000,"Frontend Engineer")


mgr1 = Manager("Lalit","Jangid",45000)
mgr1.add_employees(dev1)
mgr1.add_employees(dev2)

