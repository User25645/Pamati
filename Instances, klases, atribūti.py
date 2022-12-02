import random

class Rectangle:
    count = 0   #klases atribūts ir kopīgs visiem instancēm(rect 1, rect 2)
    def __init__(self, name, width=10, height=10, color="Blue"):
        self.width = width
        self.height = height    #atribūti
        self.color = color
        self.name = name
        Rectangle.count += 1

    def introduce(self):
        print(f"{self.name} {self.color} {self.width} x {self.height}")

    def calculate_area(self):
        print(f'The area of the rectangle is {self.width * self.height}')  


rect1 = Rectangle("Oskars", 100, 200, "Purple")  #instances atribūti
rect1.introduce() #lai nebūtu jaraksta print()
rect1.calculate_area()   #3.def

rect2 = Rectangle("Alan")
rect2.introduce()
rect2.calculate_area()

print(Rectangle.count)

print(rect1.name)  #name ir instances atribūts

#rectangles = []
#colors = ['Red', 'Green', 'Blue', 'Purple', 'Orange', 'Yellow', 'White', 'Black']

#for i in range(100):
#    rectangles.append(Rectangle(f"Name{i+1}", random.randint(1, 500), random.randint(1, 500), random.choice(colors)))

#for rectangle in rectangles:
#    print(f"{rectangle.name} {rectangle.color} {rectangle.width} x {rectangle.height}")





import random
import math

class STEM:
    def rectangle_area(width = 1, height = 1):
        if width >= 0 and height >=0:
            print(f"The area {width}x{height} is {width * height}")
        else:
            print(f"Can not calculate negative area of {width}x{height}")


    def degrees_to_radians(degrees):
        radians = degrees * (math.pi / 100)
        print(f"{degrees} degrees are {radians} radians")



for i in range(20):  #(0-19)
    w = random.randint(-20, 20)
    h = random.randint(-20, 20)
    STEM.rectangle_area(w, h)
