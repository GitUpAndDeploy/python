# Coffee machine project
water = 3000
milk = 500
coffee = 400
money = 0.0

# 1. Print report
def print_report():
    """Prints the report of the coffee machine."""
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

# 2. Check resources
def check_resources(coffee_type):
    """Checks if there are enough resources to make the coffee."""
    if coffee_type == "espresso":
        if water < 50:
            print("Sorry, there is not enough water.")
            return False
        if coffee < 18:
            print("Sorry, there is not enough coffee.")
            return False
    elif coffee_type == "latte":
        if water < 200:
            print("Sorry, there is not enough water.")
            return False
        if milk < 150:
            print("Sorry, there is not enough milk.")
            return False
        if coffee < 24:
            print("Sorry, there is not enough coffee.")
            return False
    elif coffee_type == "cappuccino":
        if water < 250:
            print("Sorry, there is not enough water.")
            return False
        if milk < 100:
            print("Sorry, there is not enough milk.")
            return False
        if coffee < 24:
            print("Sorry, there is not enough coffee.")
            return False
    return True

# 3. Process coins
def process_coins():
    """Processes the coins and returns the total amount."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

# 4. Check transaction
def check_transaction(coffee_type, payment):
    """Checks if the payment is enough for the coffee."""
    global money
    if coffee_type == "espresso":
        if payment < 1.50:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            money += 1.50
            change = payment - 1.50
            if change > 0:
                print(f"Here is your change: ${change:.2f}")
            return True
    elif coffee_type == "latte":
        if payment < 2.50:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            money += 2.50
            change = payment - 2.50
            if change > 0:
                print(f"Here is your change: ${change:.2f}")
            return True
    elif coffee_type == "cappuccino":
        if payment < 3.00:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = payment - 3.00
            if change > 0:
                print(f"Here is your change: ${change:.2f}")
            money += 3.00
            return True

# 5. Make coffee
def make_coffee(coffee_type):
    """Makes the coffee and updates the resources."""
    global water, milk, coffee
    if coffee_type == "espresso":
        water -= 50
        coffee -= 18
    elif coffee_type == "latte":
        water -= 200
        milk -= 150
        coffee -= 24
    elif coffee_type == "cappuccino":
        water -= 250
        milk -= 100
        coffee -= 24
    print(f"Here is your {coffee_type}. Enjoy!")

# 6. Coffee machine
def coffee_machine():
    """Main function to run the coffee machine."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Turning off the coffee machine.")
            break
        elif choice == "report":
            print_report()
        elif choice in ["espresso", "latte", "cappuccino"]:
            if check_resources(choice):
                payment = process_coins()
                if check_transaction(choice, payment):
                    make_coffee(choice)
        else:
            print("Invalid choice. Please try again.")
# Run the coffee machine
coffee_machine()
