class Employee:
    def __init__(self):
        self.name="vijay"
        self.id=63
        self.salary=60500
        self.dept="MLOPs"

    def works(self,depti):
        print(f"the employee {self.name}, works as {depti}.")

obj=Employee()
print(f"the employee name is {obj.name}")
print(obj.works("SDE"))