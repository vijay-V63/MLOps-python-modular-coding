class Employee:
    def __init__(self):
        self.name="vijay"
        self.id=63
        self.salary=60500
        self.dept="MLOPs"
        self.works("gamers")

    def works(self,depti):
        print(f"the employee {self.name}, works as {depti}.")

obj=Employee()
