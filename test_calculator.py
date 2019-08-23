"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 40 == calculator.addition(20, 20)

    def test_subtraction(self):
        assert 2 == calculator.subtraction(4, 2)

    def test_multiplication(self):
        assert 16 == calculator.multiplication(4, 4)

    def test_division(self):
        assert 25.0 == calculator.division(125, 5)

    def test_sqrt(self):
        assert 4 == calculator.sqrt(16)

    def test_crt(self):
        assert 2 == calculator.crt(8)

    def test_factorial(self):
        assert 120 == calculator.factorial(5)

    def test_power(self):
        assert 729 == calculator.power(9, 3)

    def test_modulus(self):
        assert 1 == calculator.modulus(4, 3)

    def test_vector_Length(self):
        assert 4.47 == calculator.vector_Length(4, 2)

    def test_cos(self):
        assert 0 == calculator.cos("degrees", 90)

    def test_sin(self):
        assert 1 == calculator.sin("degrees", 90)

    def test_tan(self):
        assert 1 == calculator.tan("degrees", 45)

    def test_acos(self):
        assert 1.05 == calculator.acos(0.5)
    
    def test_asin(self):
        assert 0.52 == calculator.asin(0.5)

    def test_atan(self):
        assert 0.46 == calculator.atan(0.5)

    
    def test_log(self):
        assert 1.58 == calculator.log(3, 2)
