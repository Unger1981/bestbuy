from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        """
        Applies a 'Second Half Price' promotion where every second item is half-priced.

        Parameters:
        product (Product): The product instance.
        quantity (int): The quantity being purchased.

        Returns:
        float: The final price after the promotion is applied.
        """
        total_price = product.price * quantity
        discount_amount = 0
        for i in range(1, quantity, 2):
            discount_amount += product.price * 0.5  
        final_price = total_price - discount_amount
        return final_price


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        """
        Applies a 'Third One Free' promotion where every third item is free.

        Parameters:
        product (Product): The product instance.
        quantity (int): The quantity being purchased.

        Returns:
        float: The final price after the promotion is applied.
        """
        total_price = product.price * quantity
        discount_amount = 0
        free_items = quantity // 3  
        discount_amount = free_items * product.price  
        final_price = total_price - discount_amount
        return final_price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        """
        Initializes the PercentDiscount promotion.

        Parameters:
        name (str): The name of the promotion.
        percent (float): The discount percentage to apply (e.g., 20 for 20%).
        """
        super().__init__(name)
        self.percent = percent / 100  
    def apply_promotion(self, product, quantity):
        """
        Applies a percentage discount to the product.

        Parameters:
        product (Product): The product instance to apply the discount to.
        quantity (int): The quantity of the product being purchased.

        Returns:
        float: The final price after the discount is applied.
        """
        total_price = product.price * quantity
        discount_amount = total_price * self.percent
        final_price = total_price - discount_amount

        return final_price


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
            self._promotion = None
        except ValueError as error:
            print(f"Wrong values for parameter used Error: {error}")

    def set_promotion(self, promotion_class):
        """_summary_

        Args:
            promotion_class (_type_): _description_
        """
        self._promotion = promotion_class

    def get_promotion(self):
        """
        Returns the promotion object of the product.
        
        Returns:
        object: The current promotion of the product or None.
        """
        return self._promotion    


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
        promo = self.get_promotion()
        return f"{self.name} Price: {self.price} Quantity: {self.quantity} Promotion:{promo}"


    def buy(self, quantity):
        """
        Processes the purchase of the specified quantity of the product, adjusting the stock accordingly. 
        Including optional promotions.
        
        Parameters:
        quantity (int): The number of items to purchase.
        
        Returns:
        str: A message indicating the success or failure of the purchase.
        """
        try:
            stock_check = self.quantity - quantity
        except ValueError as e:
            print(f"Unvalid quantity parameter used.Error: {e}")    
        if stock_check >= 0:
            self.quantity = stock_check
            promo = self.get_promotion()
            if isinstance(promo, SecondHalfPrice):
                print(f"Purchase of {quantity} units {self.name}")
                promo_price = self._promotion.apply_promotion(self,quantity)
                print(f"Promotion applied to purchase. Total is {promo_price} instead of {quantity * self.price}")
            elif  isinstance(promo, ThirdOneFree):
                print(f"Purchase of {quantity} units {self.name}")
                promo_price = self._promotion.apply_promotion(self,quantity)
                print(f"Promotion applied to purchase. Total is {promo_price} instead of {quantity * self.price}")
            elif isinstance(promo, PercentDiscount):
                print(f"Purchase of {quantity} units {self.name}")
                promo_price = self._promotion.apply_promotion(self,quantity)
                print(f"Promotion applied to purchase. Total is {promo_price} instead of {quantity * self.price}")

            else:
                return f"Purchase of {quantity}*{self.name} for {quantity * self.price} placed"
        else:
            raise ValueError (f"Cant complete order for {self.name}. Order volume {quantity} higher than stock quantity")    


class NonStockedProduct(Product):
    """_summary_

    Args:
        Product (_type_): _description_
    """
    def __init__(self, name, price ):
        super().__init__(name, price, quantity=0)
        self.quantity = 0


    def set_quantity(self):
        """
        Child method preventing changes to quantity since alway zero.
        
        Parameters:
        quantity (int): The new quantity to set.

        Return:
        string: Information about no change in quantity since non stocked product
        """
        return f"{self.name} is non stocked. Quantity always 0. "
    

    def show(self):
        """
        Displays the product details (name, price, ).
        
        Returns:
        str: A formatted string displaying the product information.
        """
        promo = self.get_promotion()
        return f"{self.name} Price: {self.price} Promotion:{promo}"
    

    def buy(self, quantity):
        """
        Processes the purchase without specified quantity of the product. Including optional Promotions.
        
        Parameters:
        quantity (int): The number of items to purchase.
        
        Returns:
        str: A message indicating the success or failure of the purchase.
        """
        promo = self.get_promotion()
        if isinstance(promo, SecondHalfPrice):
            promo_price = self._promotion.apply_promotion(self,quantity)
            print(f"Purchase of {quantity} units {self.name}")
            print(f"Promotion applied to purchase. Total is {promo_price} instead of {quantity * self.price}")
            return
        elif  isinstance(promo, ThirdOneFree):
            promo_price = self._promotion.apply_promotion(self,quantity)
            print(f"Purchase of {quantity} units {self.name}")
            print(f"Promotion applied to purchase. Total is {promo_price} instead of {quantity * self.price}")
            return
        elif isinstance(promo, PercentDiscount):
            promo_price = self._promotion.apply_promotion(self,quantity)
            print(f"Purchase of {quantity} units {self.name}")
            print(f"Promotion applied to purchase. Total is {promo_price} instead of {quantity * self.price}")
            return
        else:
            return f"Purchase of {quantity}*{self.name} for {quantity * self.price} placed"
      


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
        """
        Displays the product details (name, price, and quantity).
        
        Returns:
        str: A formatted string displaying the product information.
        """
        promo = self.get_promotion()
        return f"{self.name} Price: {self.price} Quantity: {self.quantity} Max order quantity is {self.maximum} Promotion:{promo}"
    

    def buy(self, quantity):
        """
        Processes the purchase of the specified quantity of the product, adjusting the stock accordingly. 
        Including optional promotions.
        
        Parameters:
        quantity (int): The number of items to purchase.
        
        Returns:
        str: A message indicating the success or failure of the purchase.
        """
        try:
            stock_check = self.quantity - quantity
        except ValueError as e:
            print(f"Unvalid quantity parameter used.Error: {e}")    
        if stock_check >= 0 and quantity <= self.maximum:
            self.quantity = stock_check
            promo = self.get_promotion()
            if isinstance(promo, SecondHalfPrice):
                print(f"Purchase of {quantity} units {self.name}")
                promo_price = self._promotion.apply_promotion(self,quantity)
                print(f"Promotion applied to purchase. Total is {promo_price} instead of {quantity * self.price}")
            elif  isinstance(promo, ThirdOneFree):
                print(f"Purchase of {quantity} units {self.name}")
                promo_price = self._promotion.apply_promotion(self,quantity)
                print(f"Promotion applied to purchase. Total is {promo_price} instead of {quantity * self.price}")
            elif isinstance(promo, PercentDiscount):
                print(f"Purchase of {quantity} units {self.name}")
                promo_price = self._promotion.apply_promotion(self,quantity)
                print(f"Promotion applied to purchase. Total is {promo_price} instead of {quantity * self.price}")
            else:
                return f"Purchase of {quantity}*{self.name} for {quantity * self.price} placed"
        else:
            raise ValueError (f"Cant complete order for {self.name}. Order volume {quantity} higher than stock quantity ") 
        

