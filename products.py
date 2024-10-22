class Product:
    def __init__(self, name ,price ,quantity):
        try:
            self.name = str(name)
            self.price = float(price)
            self.quantity = int(quantity)
            self.active = True
        except ValueError as error:
            print(f"Wrong values for parameter used Error: {error}")



    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        if quantity <=0:
            self.active = False


    def is_active(self):
        return self.active


    def deactivate(self):
        self.active = False


    def show(self):
        return f"{self.name} Price: {self.price} Quantity: {self.quantity}"


    def buy(self, quantity):
        try:
            stock_check = self.quantity - quantity
        except ValueError as error:
            print(f"No valid quantity added. Error {error}")    
        if stock_check >=0:
            self.quantity = stock_check
            return f"Purchase of {quantity}*{self.name} for {quantity * self.price} placed"
        else:
            return f"Cant complete order for {self.name}. Order volume {quantity} higher than stock quantity {self.quantity}"    


# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)

# mac = Product("MacBook Air M2", price=1450, quantity=100)

# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())

# bose.show()
# mac.show()

# bose.set_quantity(1000)
# bose.show()