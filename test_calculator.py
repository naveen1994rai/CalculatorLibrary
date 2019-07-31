"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.addition(2, 2)

    
    def test_subtraction(self):
        assert 2 == calculator.subtraction(4, 2)
    
    def test_multiplication(self):
        assert 8 == calculator.multiplication(2,4)

    def test_division(self):
        assert 2 == calculator.division(4,2)

    def test_sqrt(self):
        assert 4 == calculator.sqrt(16)

    def test_crt(self):
        assert 9 == calculator.crt(729)

    def test_factorial(self):
        assert 120 == calculator.factorial(5)

    def test_power(self):
        assert 8 == calculator.power(2,3)

    def test_modulus(self):
        assert 2 == calculator.modulus(8,3)

    def test_vector_Length(self):
        assert 6.40 == calculator.vector_Length(4,5)

    def test_cos(self):
        assert 1 == calculator.cos('degrees',0)

    def test_sin(self):
        assert 1 == calculator.sin('degrees',90)

    def test_tan(self):
        assert 1 == calculator.tan('degrees',45)

    def test_asin(self):
        assert 0 == calculator.asin(0)

    def test_acos(self):
        assert 1.57 == calculator.acos(0)

    def test_atan(self):
        assert 0.79 == calculator.atan(1)

    def test_var_Remove(self):
        assert None == calculator.var_Remove()

    def test_var_Store(self):
        assert 234.24 == calculator.var_Store(234.24)