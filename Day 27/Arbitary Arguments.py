def add(*args):
    print(sum(args))      #args stores data in tuples
    sum_numbers = 0
    for num in args:
        sum_numbers += num
    print(sum_numbers)

add(1,2,3,4,5)

def calculate(n,**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    for (key,value) in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=2)  #these add and multiply is the optional arguments

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")  #if we don't give model optional arguments to function in keyword arguments then it will not show error

my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
