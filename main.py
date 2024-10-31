from products import Product, NonStockedProduct, LimitedProduct, Promotion ,SecondHalfPrice, PercentDiscount ,ThirdOneFree  
from store import Store


def main():
    """
    Initializes the store with a list of products and starts the menu loop.
    
    Creates a Store instance using the product_list and passes it to the start() function
    for user interaction.
    """

    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250),
                 NonStockedProduct("Windows License", price=125),
                 LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
            ]   

    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

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
        if menu_user_input == 1:
            get_print_products(store_object)
        elif menu_user_input == 2:
            total_amount = store_object.get_total_quantity()
            print(f"Total_amount in store {total_amount} units")
        elif menu_user_input == 3:
            shopping_cart = []
            products = get_print_products(store_object)
            print("When you want to finish order, enter empty text.")
            while True:
                
                user_input_product = "0"
                user_input_quantity = "0"
                user_input_product = input("Which product do you want")
                user_input_quantity = input("What amount do you want?")
                if user_input_product == "" or user_input_quantity == "":
                        break 
                try:    
                    selected_product = products[int(user_input_product) -1]
                    shopping_cart.append((selected_product,int(user_input_quantity)))   
                except ValueError as e:
                    print(f"The entered value(s) arent integer. Error {e}")    
                except IndexError as e:
                    print(f"Entered number not in list. Error {e}")       
            order_sum = store_object.order(shopping_cart)
            print(order_sum)
        elif menu_user_input == 4:
            print("4: Exiting program...")
            break
        else:
            print("No valid selection. Please enter a number from 1-4.")


def get_print_products(store_object):
    """
    Provides a list of Product objects with all products in the store class instance.
    Iterates over all products and prints a formatted string with index, name, and quantity.

    Parameters:
    store_object (Store): An instance of the Store class containing products.

    Returns:
        list: A list of Product objects from the store.
    """
    products = store_object.get_all_products()
    for index, product in enumerate(products, 1):
        print(f"{index} {product.name} * {product.quantity} units")
    return products 


if __name__ == "__main__":
    main()




