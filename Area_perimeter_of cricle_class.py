"""

#Method 1: Area of Circle and perimeter using Math Module

import math

radius = float(input('Enter the radius of circle: '))

area = math.pi * radius ** 2

perimeter = 2 * math.pi * radius

print('Area of the circle: ',round(area,2))
print('Perimeter of the circle : ',round(perimeter,2))


"""

#Method 2: Finds the area of the circle using classes

import math
class circle():
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi *(self.radius**2)

    def perimeter(self):
        return 2*math.pi*self.radius

r = int(input('Enter the radius of circle: '))
obj = circle(r)
print('Area of circle : ',round(obj.area(),2))
print('Perimeter of circle : ',round(obj.perimeter(),2))
