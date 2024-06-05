def add(x,y):
    result=x+y
    return result
def substract(x,y):
    result=x-y
    return result
def divide(x,y):
    result = x/y
    return result
def multiply(x,y):
    result = x*y
    return result
def remainder(x,y):
    result = x%y
    return result
def power_of(x,y):
    result = x**y
    return result
def sum(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total    
def multiply_many(*numbers):
    multiply=1
    for number in numbers:
        multiply*=number
    return multiply   
