class Circle:
    def __init__(self,a,b):
        self.input1 = a
        self.input2 = b

    def area(a,b):
        if a ==b :
            print("True")
        else:
            print("false")


a = input("Enter Radius of Circle 1:")
b = input("Enter Radius of Circle 2:")


print(Circle.area(a,b))



