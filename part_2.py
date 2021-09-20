import math

class Circle:
    def __init__(self,r):
        self.radius = r

    def circumference(self):
        return 2 * math.pi * self.radius
    
    def compare_circle():
        if a>b:
            print("Circle 1 is bigger than Circle 2")
        else:
            print("Circle 2 is bigger than Circle 1")

        
a=int(input("Enter radius of circle 1 : "))
b=int(input("Enter radius of circle 2 : "))

newCircle1 = Circle(a)
newCircle2 = Circle(b)

print(f"Circumference if circle 1: {newCircle1.circumference()}")
print(f"Circumference if circle 2: {newCircle2.circumference()}")

Circle.compare_circle()
