class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def view(self):
        print(f"{self.name}: ${self.price}")

class Restaurant:
    def __init__(self, name_r):
        self.name_r = name_r
        self.menu = []
        self.orders = []

    def add_food(self, food):
        self.menu.append(food)

    def menu_view(self):
        print(f"=== {self.name_r} is menu ===")
        for i in range(len(self.menu)):
            print(f"{i + 1}.{self.menu[i].name}: ${self.menu[i].price}")

    def order(self):
        while True:
            self.menu_view()
            choice = int(input("Select a food number (0 - completion):"))
            if choice == 0:
                print("The order has been completed.")
                break
            elif 1 <= choice <= len(self.menu):
                self.orders.append(self.menu[choice-1])
                print("The order has been added.")
            else:
                print("Invalid choice.")

    def order_view(self):
        if len(self.orders) == 0:
            print("The order is empty.")
            return
        print("Your order:")
        total_amount = 0
        for order in self.orders:
            print(f"- {order.name}: {order.price}")
            total_amount += order.price
        print(f"Total amount: ${total_amount}")

    def paid(self):
        if len(self.orders) == 0:
            print("The order is empty.")
            return

        total_amount = 0
        for order in self.orders:
            total_amount += order.price

        print(f"Total amount: ${total_amount}")
        confirm = input("Do you wish to pay the order? (y/n): ").lower()
        if confirm == "y":
            print("Your order has been paid.")
            self.orders = []
        else:
            print("Your order has been cancelled.")

def main():
    restaurant = Restaurant("Yaponamama")

    restaurant.add_food(Food("Golden Fish", 8.2))
    restaurant.add_food(Food("Gohan toniku", 8.9))
    restaurant.add_food(Food("Salmon Miso soup", 6.3))
    restaurant.add_food(Food("Ramen with beef", 6.5))
    restaurant.add_food(Food("Udon with chicken", 4.9))
    restaurant.add_food(Food("Udon with beef", 5.5))

    while True:
        print("Welcome to the restaurant menu")
        print("1.Menu view")
        print("2.Order")
        print("3.Order view")
        print("4.Paid")
        print("5.Exit")

        choice = int(input("Select a menu number: "))

        if choice == 1:
            restaurant.menu_view()
        elif choice == 2:
            restaurant.order()
        elif choice == 3:
            restaurant.order_view()
        elif choice == 4:
            restaurant.paid()
        elif choice == 5:
            print("Exited the program.")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()