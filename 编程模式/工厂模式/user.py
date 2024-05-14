from factory import CalculatorFactory

add_calculator = CalculatorFactory.create_add_calculator()

print(add_calculator.func(1,2))
