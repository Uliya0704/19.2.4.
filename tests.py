import pytest
from app.calc import Calculator
class TestCalc:
    def setup (self):
        self.calc=Calculator
    def test_adding_success(self):
        assert self.calc.adding(self, 5, 7)==12

    def test_multiply_saccess(self):
        assert self.calc.multiply(self, 5, 6)==30

    def test_division_saccess(self):
        assert self.calc.division(self, 40, 4)==10

    def test_subtraction_saccess(self):
        assert self.calc.subtraction(self, 50, 7)==43

    def test_adding_success(self):
        assert self.calc.adding(self, 5, -10)==-5

    def test_subtraction_saccess(self):
        assert self.calc.subtraction(self, 7, 50)==-43

    def test_multiply_saccess(self):
        assert self.calc.multiply(self, 5, -6)==-30

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
             self.calc.division(self, 5, 0)

    def test_division_saccess(self):
        assert self.calc.division(self, 4, 5)==0.8

    def test_dell_saccess(self):
        assert self.calc.dell(self, 4, 2)==2

    def test_stepen_saccess(self):
        assert self.calc.stepen(self, 4, 2) == 16