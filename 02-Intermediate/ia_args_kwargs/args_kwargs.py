def add(*args):
    print(sum(args))


add(2, 4, 3, 2, 2)


def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Toyota", model="GR86")
print(my_car.make, my_car.model)
