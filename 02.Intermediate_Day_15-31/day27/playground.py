def add(*args): # you can actually use anything after *, like *numbers works too.
    # args is shorten of "arguments"
    for n in args:
        print(args[0])
        return sum(args)

a = add(13,10,12,14)
print(a)

def calculate(**kwargs): # kwargs = keyword argument
    print(type(kwargs))
    print(kwargs["add"])

calculate(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Toyota")

print(my_car.model)
