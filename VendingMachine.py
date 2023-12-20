#create vending machine using python

print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ███╗░░░███╗██╗░░░██╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ████╗░████║╚██╗░██╔╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ██╔████╔██║░╚████╔╝░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██║╚██╔╝██║░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░╚═╝░██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░

██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")
print("__________________________________________________________________________________________________________________")
class VendingMachine:
    def __init__(self):
        self.items = {'1': {'name': '7up', 'price': 2, 'quantity': 10},
                      '2': {'name': 'Chips', 'price': 1.50, 'quantity': 8},
                      '3': {'name': 'Chocolate', 'price': 3.50, 'quantity': 15},
                      '4': {'name': 'sandwich', 'price': 3.00, 'quantity': 5},
                      '5': {'name': 'water', 'price': 1.00, 'quantity': 40},
                      '6': {'name': 'break', 'price': 0.50, 'quantity': 20},
                      '7': {'name': 'cookie', 'price': 1.50, 'quantity': 10},
                      '8': {'name': 'KitKat', 'price': 1.50, 'quantity': 8},
                      '9': {'name': 'protein bar', 'price': 1.00, 'quantity': 25},
                      '10': {'name': 'candy', 'price': 1.25, 'quantity': 20}}
        self.balance = 0

    def display_items(self):
        print("Available items:")
        for code, item in self.items.items():
            print(f"{code}. {item['name']} - ${item['price']:.2f} - Quantity: {item['quantity']}")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted: ${amount:.2f}, Total Balance: ${self.balance:.2f}")

    def purchase_item(self, item_code):
        if item_code in self.items:
            item = self.items[item_code]
            if item['quantity'] > 0 and self.balance >= item['price']:
                self.balance -= item['price']
                item['quantity'] -= 1
                print(f"Purchased {item['name']} for ${item['price']:.2f}. Remaining Balance: ${self.balance:.2f}")

                # Ask if the user wants to purchase anything else
                while True:
                    purchase_more = input("Do you want to purchase anything else? (yes/no): ").lower()
                    if purchase_more == 'no':
                        print("""
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗  ██╗    ██╗░░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║  ╚═╝    ╚██╗░
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║  ░░░    ░╚██╗
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║  ░░░    ░██╔╝
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝  ██╗    ██╔╝░
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝    ╚═╝░░""")
                        return  # Exit the purchase_item method
                    elif purchase_more == 'yes':
                        self.display_items()  # Display items again
                        return  # Exit the purchase_item method
                    else:
                        print("Invalid choice. Please enter 'yes' or 'no'.")
            else:
                print("Insufficient balance or item out of stock.")
        else:
            print("Invalid code.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0


def main():
    vending_machine = VendingMachine()

    while True:
        print("\nOptions:")
        print("1. Display Items")
        print("2. Insert Money")
        print("3. Purchase Item")
        print("4. Return Change")
        print("5. Exit")
        print("____________________________________________________________")

        choice = input("Enter your choice: ")

        if choice == '1':
            vending_machine.display_items()
        elif choice == '2':
            amount = float(input(" insert money: $"))
            vending_machine.insert_money(amount)
        elif choice == '3':
            item_code = input("Enter the item code: ")
            vending_machine.purchase_item(item_code)
        elif choice == '4':
            vending_machine.return_change()
        elif choice == '5':
            print("")
            break
        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
