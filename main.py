from products import Product
from store import Store



product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]


def main():               
    best_buy = Store(product_list)
    start(best_buy)

def start(store_object): 
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")   
    while True:
        try:
            menu_user_input = int(input("Enter from 1-4 "))
        except ValueError as e:
            print(f"Invalid Input. Error {e}")
        if menu_user_input == 1:
                print("1")
        elif menu_user_input == 2:
                print("2")
        elif menu_user_input == 3:
                print("3")
        elif menu_user_input == 4:
                print("4")
                break
        else:
            print("No valid selection")


if __name__ == "__main__":
    main()

    
       