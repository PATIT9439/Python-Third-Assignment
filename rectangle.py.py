class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    
    def rectangle_area(self):
        return self.length*self.width

a=int(input("Enter length of rectangle: "))
b=int(input("Enter breath of rectangle: "))

newRectangle = Rectangle(a,b)
print(f"Area of rectangle: {newRectangle.rectangle_area()}")
        