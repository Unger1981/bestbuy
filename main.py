from products import Product
from store import Store

def main():
    """
    Initializes the store with a list of products and starts the menu loop.
    
    Creates a Store instance using the product_list and passes it to the start() function
    for user interaction.
    """

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    
    best_buy = Store(product_list)

    shopping_cart = [(product_list[0], 1), (product_list[1], 1)]

    start(best_buy,shopping_cart)
   


def start(store_object, shopping_cart):
    """
    Provides a menu for interacting with the store and handles user input.
    
    Parameters:
    store_object (Store): An instance of the Store class containing products.
    """
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")   
   
    while True:
        try:
            menu_user_input = int(input("Enter a number from 1-4: "))
        except ValueError as e:
            print(f"Invalid Input. Error: {e}")
            continue
        
        if menu_user_input == 1:
            products = store_object.get_all_products()
            for index, product in enumerate(products,1):
                print(f"{index} {product.name} * {product.quantity} units")
        elif menu_user_input == 2:
            total_amount = store_object.get_total_quantity()
            print(f"Total_amount in store {total_amount} units")
        elif menu_user_input == 3:
            order_sum = store_object.order(shopping_cart)
            print(order_sum)
        elif menu_user_input == 4:
            print("4: Exiting program...")
            break
        else:
            print("No valid selection. Please enter a number from 1-4.")


if __name__ == "__main__":
    main()
