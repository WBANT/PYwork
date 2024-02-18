class Student:
    def __init__(self, name, year_level, house):
        self.name = name
        self.year_level = year_level
        self.house = house

    def introduction(self):
        print(f"Hello my name is {self.name}, my year level is {self.year_level} and my house is {self.house}")

    
bob = Student("Bob", "year 11", "Smale")
Antony = Student("Antony", "year 13", "Pupuke")
Alex = Student("Alex", "year 13", "Pupuke")
Minjae = Student("Minjae", "year 13", "Murchison")
Jamie = Student("Jamie", "year 13", "Hood")

#print(bob.house)
bob.introduction()

class Car:
    def __init__(self, make, model, year, current_speed)
        self.make = make
        self.model = model
        self.year = year
        self.current_speed = current_speed

    def start(self):
        print(f"Starting the {self.make} {self.year} {self.model} ")

    def speedometer(self):
        print(f"Current speed is: {self.current_speed}")
    
    def vehicle(self):
        print(f"Make: {self.make} Model: {self.model} Year: {self.year} Current speed: {self.current_speed} ")

    def accel(self):
        originspeed = 0
        beginaccel = input("How fast do you want to accelerate?")
        totalaccel = beginaccel + originspeed

    def deccel(self):
        originspeed = 0
        begindeccel = input("How much speed do you want to ?")
        totaladeccel = begindeccel + originspeed


input()
