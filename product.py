#Your program should have two separate classes: one to represent a product to be purchased and one to represent a shopping cart containing a collection of products.

# Each product has a name, base price, and tax rate. There should also be a method to calculate and return the product's total price based on the base price and tax rate.

# Each shopping cart has a collection of products. It should also have the following functionality:

# add an product to the cart
# remove an product from the cart
# add up the total cost of all products in the cart before tax
# add up the total cost of all products in the cart after tax
# Think about which class needs to make reference to the other one and remember to use a import statement accordingly. You don't need it in both files.

class Product:
    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate
    def calc_price(self):
        return(self.base_price * (1+self.tax_rate))
    def __str__(self):
        return(f'Item: {self.name}, Price: {self.base_price}, Tax rate {self.tax_rate*100}%')


# bear = Product("bear", 10, 0.05)
# print(bear.base_price)
# print(bear.calc_price())