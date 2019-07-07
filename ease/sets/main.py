from numbers import Number
import random, string

def replace(main, item, new):
    output = []
    for thing in main:
        if thing == item:
            output.append(new)
        else:
            output.append(thing)
    return output
def list_type(main, instance):
    for item in main:
        if not isinstance(item, instance):
            return False
    return True
def list_types(main, instances):
    for item in main:
        items = False
        for instance in instances:
            if isinstance(item, instance):
                items = True
        if items == False:
            return False
    return True
def get_instances(main, instance):
    result = 0
    for item in main:
        if isinstance(item, instance):
            result += 1
    return result
def check_set(check):
    for x, y in check.items():
        print(x, y)
        if not isinstance(x, y):
            return False
    return True
class Person:
    def __init__(self, name):
        self.name = name
    def full_name(self):
        return name
    def first_name(self):
        return first_name.split(" ")[0]
    def middle_name(self):
        if len(first_name.split(" ")) > 2:
            return " ".join(first_name.split(" ")[1:len(first_name.split(" ") - 1)])
    def last_name(self):
        return first_name.split(" ")[:-1]
class Employee(Person):
    class Job:
        def __init__(self, employee):
            self.employee = employee
        def pay(self):
            return {"$/month": self.employee.payMonth,
            "$/year": self.employee.payMonth * 12}        
    def __init__(self, name, job, payMonth):
        super().__init__(name)
        self.job = job
        self.payMonth = payMonth
    def job(self):
        return Employee.Job(self)
    def pay(self):
        return self.job().pay()
print(super(Employee))
