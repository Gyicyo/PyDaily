from typing import Any


class calculator:

    def __init__(self,method):
        self.method = method.upper()

    def func(self,a,b):
        if self.method == "A":
            return self._add(a,b)
        elif self.method == "S":
            return self._sub(a,b)
        elif self.method == "M":
            return self._mul(a,b)
        elif self.method == "D":
            return self._div(a,b)
        else:
            return "Invalid method"

    def _add(self,a,b):
        return a+b

    def _sub(self,a,b):
        return a-b

    def _mul(self,a,b):
        return a*b

    def _div(self,a,b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a/b
