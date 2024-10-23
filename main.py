from products import Product
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]


def main():
    """
    Initializes the store with a list of products and starts the menu loop.
    
    Creates a Store instance using the product_list and passes it to the start() function
    for user interaction.
    """
    best_buy = Store(product_list)
    start(best_buy)


def start(store_object):
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
            print("1: Listing all products...")
        elif menu_user_input == 2:
            print("2: Showing total amount in store...")
        elif menu_user_input == 3:
            print("3: Making an order...")
        elif menu_user_input == 4:
            print("4: Exiting program...")
            break
        else:
            print("No valid selection. Please enter a number from 1-4.")


if __name__ == "__main__":
    main()
