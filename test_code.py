import math

def modulo(value, other):
    result =  value % other
    return print(result)

modulo(100,20)


def exponen(value, other):
    result =  value ** other
    return print(result)

exponen(6,3)

def squart(number):
    result = math.sqrt(number)
    return print(result)

squart(25)

def loga(number):
    result = math.log(number)
    return print(result)

loga(100)

def picalc(radius):
    area = math.pi*radius ** 2
    return print(area)

picalc(100)


def sinmath(angle):
    result = math.sin(math.radians(angle))
    return print(result)

sinmath(45)

def cosmath(angle):
    result = math.cos(math.radians(angle))
    return print(result)

cosmath(45)

def tanmath(angle):
    result = math.tan(math.radians(angle))
    return print(result)

tanmath(45)


def tanmath(angle):
    result = math.tan(math.radians(angle))
    return print(result)

tanmath(45)

def abs(number):
    result = math.fabs(number)
    return print(result)

tanmath(-10)


def factorial(n):
    return math.prod(range(1, n+1))
