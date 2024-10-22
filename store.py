from products import Product

class Store:

    list_of_products = []
    items_in_store = 0

    def __init__(self, products):
        for product in products:
            self.list_of_products.append(product)

    def add_product(self, product):
        try:
            self.list_of_products.append(product)
            self.items_in_store += product.quantity
            print(f"{self.items_in_store} items in store")
        except Exception as error:  
            print(error)
            


    def remove_product(self, product):
        if product in self.list_of_products:
            self.list_of_products.remove(product)
            print(self.list_of_products)
        else:
            print(f"{product} not found in store")    



    def get_total_quantity(self):
        return self.items_in_store


    def get_all_products(self): 
        list_active_products= []
        for product in self.list_of_products:
            if product.active == True:
                list_active_products.append(product)
        return list_active_products        


    def order(self,shopping_list):
        total_price = 0
        for product ,quantity in shopping_list:
            if product in self.list_of_products:
                product.buy(quantity)
                self.items_in_store -= quantity
                total_price += product.price * quantity
                
            else:  
                print("Product not found in stock") 
        return total_price        





product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))