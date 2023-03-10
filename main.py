import time
import os

def timetracker(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f"Execution process took {t2} seconds.")
    return wrapper
    
@timetracker
def task():
    subtract = lambda x, y: x-y
    add = lambda x, y: x+y
    multiply = lambda x, y: x*y
    divide = lambda x, y: x/y

    x = int(input("Enter a base number: "))
    y = int(input("Enter a second number: "))
    os.system('clear')
    time.sleep(.1)

    print("Addition:")
    print(add(x, y))
    print("Subtraction:")
    print(subtract(x, y))
    print("Multiplication:")
    print(multiply(x, y))
    print("Division:")
    print(divide(x, y))
task()
