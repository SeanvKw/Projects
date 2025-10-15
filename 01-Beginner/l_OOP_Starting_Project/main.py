from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# car = carblueprint()
#    ^         ^
#  Object    Class
#  car.speed
#   ^       ^
# Object Attribute
#  car.stop()
#   ^      ^
# Object Method
is_on = True

menu = Menu()
resources = CoffeeMaker()
money = MoneyMachine()

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        resources.report()
        money.report()
    elif choice == "refill":
        resources.refill()
        print("*YOU'VE USED ADMIN PRIVELAGES LOL, WITH IMAGINATION U JUST REFILLED WHOLE COFFE MACHINE*")
    else:
        drink = menu.find_drink(choice)
        # musi być drink and etc. żeby uniknąć błędu NoneType
        if drink and resources.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                resources.make_coffee(drink)
