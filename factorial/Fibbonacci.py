class Factorial:

    def __init__(self):
        self.log = {}

    def factorial(self, num):
        print(num)
        if num in [0, 1]:
            return 1

        if num in self.log:
            return self.log[num]
        self.log[num] = num * self.factorial(num - 1)

        return self.log[num]
