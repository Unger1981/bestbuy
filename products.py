
class Product:
    """
    A class representing a product with a name, price, quantity, and active status.
    
    Attributes:
    name (str): The name of the product.
    price (float): The price of the product.
    quantity (int): The quantity of the product available.
    active (bool): The status of the product (active/inactive).
    """

    def __init__(self, name ,price ,quantity):
        """
        Initializes a new Product instance with name, price, and quantity.
        
        Parameters:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity available for the product.
        """
        if not name:
            raise ValueError("Product name cannot be empty")
        if price <= 0:
            raise ValueError("Price must be positive")
        try:
            self.name = str(name)
            self.price = float(price)
            self.quantity = int(quantity)
            self.active = True
        except ValueError as error:
            print(f"Wrong values for parameter used Error: {error}")


    def get_quantity(self):
        """
        Returns the quantity of the product.
        
        Returns:
        int: The current quantity of the product.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Updates the quantity of the product. If the quantity is less than or equal to 0,
        the product is marked as inactive.
        
        Parameters:
        quantity (int): The new quantity to set.
        """
        self.quantity -= quantity
        if self.quantity <=0:
            self.active = False


    def is_active(self):
        """
        Checks if the product is active.
        
        Returns:
        bool: True if the product is active, False otherwise.
        """
        return self.active


    def deactivate(self):
        """
        Deactivates the product by setting its active status to False.
        """
        self.active = False


    def show(self):
        """
        Displays the product details (name, price, and quantity).
        
        Returns:
        str: A formatted string displaying the product information.
        """
        return f"{self.name} Price: {self.price} Quantity: {self.quantity}"


    def buy(self, quantity):
        """
        Processes the purchase of the specified quantity of the product, adjusting the stock accordingly.
        
        Parameters:
        quantity (int): The number of items to purchase.
        
        Returns:
        str: A message indicating the success or failure of the purchase.
        """
        try:
            stock_check = self.quantity - quantity
        except ValueError as e:
            print(f"Unvalid quantity parameter used.Error: {e}")    
        if stock_check >=0:
            self.quantity = stock_check
            return f"Purchase of {quantity}*{self.name} for {quantity * self.price} placed"
        else:
            raise ValueError (f"Cant complete order for {self.name}. Order volume {quantity} higher than stock quantity {self.quantity}")    


class NonStockedProduct(Product):
    def __init__(self, name, price,quantity = 0 ):
        super().__init__(name, price, quantity = 0 )
        self.quantity = 0


    def set_quantity(self, quantity):
        """
        Child method preventing changes to quantity since alway zero.
        
        Parameters:
        quantity (int): The new quantity to set.

        Return:
        string: Information about no change in quantity since non stocked product
        """
        return f"{self.name} is non stocked. Quantity always 0"
    
    def show(self):
        """
        Displays the product details (name, price, ).
        
        Returns:
        str: A formatted string displaying the product information.
        """
        return f"{self.name} Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        stock_check = self.quantity - quantity
        if stock_check >= 0:
            if quantity > self.maximum:
                return f"The order exceeds the allowed maximum of {self.maximum} for {self.name}"
            else:
                self.quantity = stock_check
                return f"Purchase of {quantity}*{self.name} for {quantity * self.price} placed"
        else:
            raise ValueError(f"Cannot complete order for {self.name}. Order volume {quantity} exceeds stock {self.quantity}")

    def show(self):
        return f"{self.name} Price: {self.price} Quantity: {self.quantity} Max order quantity: {self.maximum}"   



    
    def show(self):
        """
        Displays the product details (name, price, and quantity).
        
        Returns:
        str: A formatted string displaying the product information.
        """
        return f"{self.name} Price: {self.price} Quantity: {self.quantity} Max order quantity is {self.maximum}"
    

