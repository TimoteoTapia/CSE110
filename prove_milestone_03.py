"""
File: Milestone
Author: Timoteo Tapia
"""
class Meal_price:
    #get the inputs of everything
    def __init__(self):
        print()
        self.child_meal = float(input("what is the price of a child's meal? ".capitalize()))
        self.adult_meal = float(input("what is the price of an adult's meal? ".capitalize()))
        self.children = int(input("how many children are there? ".capitalize()))
        self.adults = int(input("how many adults are there? ".capitalize()))
        self.get_tax = float(input("what is the sales tax rate? "))
        self.total = 0
        self.tax = 0
    #get the subtotal
    def subtotal(self):
        print()
        self.total = self.child_meal * self.children + self.adult_meal * self.adults
        print("Subtotal: ${}".format(round(self.total,2)))
    #get the tax
    def sales_tax(self):
        self.tax = self.total * self.get_tax / 100
        print("Sales Tax: ${}".format(round(self.tax,2)))
    #get the total
    def total_ouput(self):
        self.total = self.tax + self.total
        print("Total: ${}".format(round(self.total,2)))
    #get the change for the user
    def change(self):
        print()
        payment = float(input("what is the payment amount? "))
        print(f"Change: ${round(payment - self.total,2)}")
        print()
    #get all the data for a product(xbox oane)
    def xbox(self):
        print()
        new_xbox = float(input("what is the price of a xbox one in your country? ".capitalize()))
        controller = float(input("what is the price of a xbox one controller in your country? ".capitalize()))
        controller_num = int(input("how many controllers do you want? ".capitalize()))
        self.total = new_xbox + controller * controller_num
        self.tax = self.total * self.get_tax / 100
        print()
        print("Subtotal: ${}".format(round(self.total,2)))
        print("Sales Tax: ${}".format(round(self.tax,2)))
        self.total = self.tax + self.total
        print("Total: ${}".format(round(self.total,2)))

meal_price = Meal_price()
meal_price.subtotal()
meal_price.sales_tax()
meal_price.total_ouput()
meal_price.change()
if (input("Would you like to make more shopping [y/n] ")) == "y":
    meal_price.xbox()
    meal_price.change()
