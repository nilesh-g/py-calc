
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def square(a):
    return a * a
def cube(a):
    return a ** 3

if __name__ == '__main__':
    print("add() - ", add(1, 2))
    print("subtract() - ", subtract(1, 2))
    print("multiply() - ", multiply(1, 2))
    print("divide() - ", divide(1, 2))
    print("square() - ", square(1))

    print("cube() - ", cube(3))
