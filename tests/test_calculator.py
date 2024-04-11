import unittest
from src.calculator import Calculator
from typing import NoReturn
from src.custom_ex import IncorrectInputError

class CalculatorAddTestCase(unittest.TestCase):  # Test Case
    def setUp(self):
        self.calculator = Calculator()

    def test_add_3_corrrect_input(self) -> None | NoReturn:  # Unit
        # Arrange

        x = 4
        y = 3
        z = 1
        expected_result = 8

        # Act
        result = self.calculator.add(x, y, z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_no_args(self) -> None | NoReturn:
        # Arrange

        expected_result = 0

        # Act
        result = self.calculator.add()

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_incorrect_input(self) -> NoReturn:
        # Arrange

        x = "6"
        y = [4, 5]

        # Act/Assert
        with self.assertRaises(TypeError):
            self.calculator.add(x, y)

class CalculatorMultTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_mult_with_correct_input(self):
        # Arrange
        x = 1
        y = 2
        z = 3
        expected_result = 6

        # Act
        result = self.calculator.multiply(x, y, z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_mult_with_incorrect_input(self):
        # Arrange
        x = []
        y = (1, 2)
        z = "4"

        # Act/Assert
        with self.assertRaises(IncorrectInputError):
            self.calculator.multiply(x, y, z)

    def tearDown(self):
        pass

class CalculatorSubsTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_subs_with_correct_input(self):
        # Arrange
        x = 5
        y = 2

        expected_result = 3

        # Act
        result = self.calculator.substraction(x, y)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorDivTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_div_with_correct_input(self):
        # Arrange
        x = 10
        y = 5

        expected_result = 2

        # Act
        result = self.calculator.division(x, y)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorModTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_mod_with_correct_input(self):
        # Arrange
        x = 100
        y = 20

        expected_result = 0

        # Act
        result = self.calculator.modulo(x, y)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorExpoTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_expo_with_correct_input(self):
        # Arrange
        x = 6
        y = 3

        expected_result = 216

        # Act
        result = self.calculator.exponen(x, y)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorSquTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_squ_with_correct_input(self):
        # Arrange
        num = 25

        expected_result = 5.0

        # Act
        result = self.calculator.squart(num)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorLogTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_log_with_correct_input(self):
        # Arrange
        num = 100

        expected_result = 4.605170185988092

        # Act
        result = self.calculator.loga(num)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorSinTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_sin_with_correct_input(self):
        # Arrange
        num = 45

        expected_result = 0.7071067811865475

        # Act
        result = self.calculator.sinmath(num)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorCosTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_cos_with_correct_input(self):
        # Arrange
        num = 45

        expected_result = 0.7071067811865476

        # Act
        result = self.calculator.cosmath(num)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorTanTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_tan_with_correct_input(self):
        # Arrange
        num = 45

        expected_result = 0.9999999999999999

        # Act
        result = self.calculator.tanmath(num)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorAbsTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_abs_with_correct_input(self):
        # Arrange
        num = -10

        expected_result = 10

        # Act
        result = self.calculator.abs(num)

        # Assert
        self.assertEqual(result, expected_result)

class CalculatorFacTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_fac_with_correct_input(self):
        # Arrange
        num = 5

        expected_result = 120

        # Act
        result = self.calculator.factorial(num)

        # Assert
        self.assertEqual(result, expected_result)
