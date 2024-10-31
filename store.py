from products import Product, NonStockedProduct, LimitedProduct, Promotion ,SecondHalfPrice, PercentDiscount ,ThirdOneFree

class Store:
    """
    A class representing a store containing multiple products.

    Attributes:
    list_of_products (list): A list of all products in the store.
    items_in_store (int): The total number of items in the store.
    """

    list_of_products = []
    items_in_store = 0


    def __init__(self, products):
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
                    if quantity <= product.quantity and not isinstance(product,NonStockedProduct):
                        product.buy(quantity)
                        self.items_in_store -= quantity   
                        total_price += quantity * product.price
                    else:
                        if isinstance(product,NonStockedProduct):
                            product.buy(quantity)
                        else:
                            print("Stock not sufficient for order quantity")    
                else:  
                    print(f"Product {product} not found in stock")
            print(f"Total amount = {total_price}")        
        except ValueError as e:
            print(f"Total amount = {total_price}")
            print(f"Wrong product and/or quantity entered during order. Error: {e}")
    




# product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
#                  Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                  Product("Google Pixel 7", price=500, quantity=250),
#                  NonStockedProduct("Windows License", price=125),
#                  LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
#             ]   

# second_half_price = SecondHalfPrice("Second Half price!")
# third_one_free = ThirdOneFree("Third One Free!")
# thirty_percent = PercentDiscount("30% off!", percent=30)

# product_list[0].set_promotion(second_half_price)
# product_list[1].set_promotion(third_one_free)
# product_list[3].set_promotion(thirty_percent)

# new_store =Store(product_list)

# new_store.order([(product_list[3],10)])