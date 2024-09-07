from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# todo read through the document provided
# todo understand each class methods and attribute. MenuItem class has only attributes -> now I understand most of them

m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

item = MenuItem("latte", 100,200,30,2)
print(item.ingredients)

print(m.get_items()) # latte/espresso/cappuccino/
print(m.find_drink("latte").ingredients) # {'water': 200, 'milk': 150, 'coffee': 24}

cm.report()
print(cm.is_resource_sufficient(m.find_drink("latte"))) # true
cm.make_coffee(m.find_drink("latte")) # Here is your latte ☕️. Enjoy!

mm.report()
enough_or_not = mm.make_payment(2)
print(enough_or_not) # true or false

