""""
Areas of Shapes: Getting the areas and volumes of different shapes
Author: Timoteo Tapia
"""
import math

def main():
    square()
    rectangle()
    circle()
    sphere_and_more()

def square():
    print()
    square = float(input("what is the length of a side of the square? ".capitalize()))
    print("The area of the square in centimeters is: {} cm^2.".format(square * square))
    print("The area of the square in centimeters is: {} m^2.".format(square ** 2 /10000))


def rectangle():
    print()
    rectangle_length = float(input("what is the length of rectangle "))
    rectangle_width = float(input("what is the width of the rectangle ".capitalize()))
    rectangle = rectangle_length * rectangle_width
    print("The area of the rectangle in centimeters is: {} cm^2.".format(rectangle))
    print("The area of the rectangle in meters is: {} m^2.".format(rectangle /10000))

def circle():
    print()
    circle = float(input("what is the radius of the circle "))
    circle = round(circle ** 2 * math.pi, 2)
    print("The area of the circle in centimeters is: {} cm^2.".format(circle))
    print("The area of the circle in meters is: {} m^2.".format(circle /10000))

def sphere_and_more():
    print()
    length = int(input("please enter another length value:  ".capitalize()))
    area_circle = round(length ** 2 * math.pi, 2)
    sphere_volume = round(length ** 3 * math.pi * 4/3, 2)
    print(f'\nThe area of the square with that side length is: {length ** 2}.')
    print(f'The area of the circle with that radius is: {area_circle}.')
    print(f'The volume of a cube with that side length is: {length ** 3}.')
    print(f'The volume of a sphere with that radius is: {sphere_volume}.\n')

main()