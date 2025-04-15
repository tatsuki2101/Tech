import calc

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a):
        self.result = calc.add(self.result, a)

    def subtract(self, a):
        self.result = calc.subtract(self.result, a)

    def multiply(self, a):
        self.result = calc.multiply(self.result, a)

    def divide(self, a):
        try:
            self.result = calc.divide(self.result, a)
        except ValueError as e:
            raise ValueError("division error") from e

    def result(self):
        return self.result

    def reset(self):
        self.result = 0
        