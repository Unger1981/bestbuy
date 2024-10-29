from products import Product

class Store:
    """
    A class representing a store containing multiple products.

    Attributes:
    list_of_products (list): A list of all products in the store.
    items_in_store (int): The total number of items in the store.
    """

    list_of_products = []
    items_in_store = 0


    def __init__(self, products=None):
        """
        Initializes a store instance with an optional list of products.

        Parameters:
        products (list, optional): A list of Product instances to add to the store.
        """
        try:
            if products is not None:
                for product in products:
                    self.list_of_products.append(product)
                    self.items_in_store += product.quantity
        except ValueError as e:
            print(f"The parameter is not valid for class creation. Error: {e}")  


    def add_product(self, product):
        """
        Adds a product to the store and updates the total item count.

        Parameters:
        product (Product): The product to be added to the store.
        """
        try:
            self.list_of_products.append(product)
            self.items_in_store += product.quantity
            print(f"{self.items_in_store} items in store")
        except AttributeError as error:  
            print(f"Product is missing required attributes. Error: {error}")


    def remove_product(self, product):
        """
        Removes a product from the store if it exists.

        Parameters:
        product (Product): The product to be removed from the store.
        """
        if product in self.list_of_products:
            self.list_of_products.remove(product)
            print(self.list_of_products)
        else:
            print(f"{product} not found in store")


    def get_total_quantity(self):
        """
        Returns the total number of items in the store.

        Returns:
        int: The total quantity of all products in the store.
        """
        return self.items_in_store
    
                                     
    def get_all_products(self): 
        """
        Returns a list of all active products in the store.

        Returns:
        list: A list of active Product instances in the store.
        """
        list_active_products = []
        try:
            for product in self.list_of_products:
                if product.active:
                    list_active_products.append(product)
        except:  
            print("No active products found.")          
        return list_active_products     
       

    def order(self, shopping_list):
        """
        Processes an order from a shopping list and updates the store's stock.

        Parameters:
        shopping_list (list): A list of tuples where each tuple contains a Product instance and a quantity to order.

        Returns:
        float: The total price of the order.
        """
        total_price = 0
        try:

            for product, quantity in shopping_list:
                if product in self.list_of_products: 
                    if quantity <= product.quantity:
                        purchase_confirm = product.buy(quantity)
                        self.items_in_store -= quantity
                        total_price += product.price * quantity
                        print(purchase_confirm)
                    else:
                        
                        print("Stock not sufficient for order quantity")    
                else:  
                    print(f"Product {product} not found in stock")
        except ValueError as e:
            print(f"Wrong product and/or quantity entered during order. Error: {e}")
        return f"Total price of purchase: {total_price}"



