# our program should have two separate classes: one to represent a product to be purchased and one to represent a shopping cart containing a collection of products.

# Each product has a name, base price, and tax rate. There should also be a method to calculate and return the product's total price based on the base price and tax rate.

# Each shopping cart has a collection of products. It should also have the following functionality:

# add an product to the cart
# remove an product from the cart
# add up the total cost of all products in the cart before tax
# add up the total cost of all products in the cart after tax
# Think about which class needs to make reference to the other one and remember to use a import statement accordingly. You don't need it in both files.

from product import Product

class Cart:
    def __init__(self, products=[]):
        self.products = products
    
    def cost_before_tax(self):
        total = 0
        for item in self.products:
            total += item.base_price
        return(total)
    def cost_after_tax(self):
        total = 0
        for item in self.products:
            total += item.calc_price()
        return(total)
    def add_to_cart(self, newitem):
        self.products.append(newitem)

    def remove_from_cart(self,rm_item_index):
        self.products.pop(rm_item_index)

    def display_cart(self):
        print("Your Cart:")
        for item in self.products:
            print(item)
newcart = Cart()

# bear = Product("bear", 10, 0.05)
# print(bear.base_price)
# print(bear.calc_price())

newcart.add_to_cart(Product("bear", 10, 0.05))
newcart.add_to_cart(Product("ball", 5, 0.14))
newcart.add_to_cart(Product("bike", 150, 0.13))

newcart.display_cart()
print(newcart.cost_before_tax())
print(newcart.cost_after_tax())

newcart.remove_from_cart(1)

newcart.display_cart()
print(newcart.cost_before_tax())
print(newcart.cost_after_tax())