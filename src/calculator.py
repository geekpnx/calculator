from .custom_ex import IncorrectInputError
import math

# Addition (+) √
# Subtraction (-) √
# Multiplication (*) √
# Division (/) √
# Modulo (%) √
# Exponentiation (^ or ** in some programming languages) √
# Square Root (sqrt()) √
# Logarithm (log()) √
# Trigonometric Functions (sin(), cos(), tan(), etc.) √
# Absolute Value (abs()) √
# Factorial (!)


class Calculator:
    def add(self, *args: float) -> float:  # type: ignore
        return sum(args)

    def multiply(self, *args: float):  # (1,2,3)
        try:
            result: float = 1
            for i in args:
                result *= i
            return result
        except TypeError:
            raise IncorrectInputError("Wrong Input")

    def substraction(self, value, other):
        result =  value - other
        return result

    def division(self, value, other):
        result =  value / other
        return result

    def modulo(self, value, other):
        result =  value % other
        return result

    def exponen(self, value, other):
        result =  value ** other
        return result

    def squart(self, number):
        result = math.sqrt(number)
        return result

    def loga(self, number):
        result = math.log(number)
        return result

    def sinmath(self, angle):
        result = math.sin(math.radians(angle))
        return result

    def cosmath(self, angle):
        result = math.cos(math.radians(angle))
        return result

    def tanmath(self, angle):
        result = math.tan(math.radians(angle))
        return result

    def abs(self, number):
        return math.fabs(number)

    def factorial(self, number):
        return math.prod(range(1, number+1))