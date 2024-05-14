from calculator import calculator

class CalculatorFactory:

    @staticmethod
    def create_add_calculator():
        return calculator(method='a')

    @staticmethod
    def create_sub_calculator():
        return calculator(method='s')

    @staticmethod
    def create_mul_calculator():
        return calculator(method='m')

    @staticmethod
    def create_div_calculator():
        return calculator(method='d')
