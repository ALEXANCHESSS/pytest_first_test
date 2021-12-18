from app.calculator import Calculator
import pytest


class TestCalculation:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calc_correct(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_substaction_calc_correct(self):
        assert self.calc.subtraction(self, 8, 2) == 6

    def test_adding_calc_correct(self):
        assert self.calc.adding(self, 4, 4) == 8