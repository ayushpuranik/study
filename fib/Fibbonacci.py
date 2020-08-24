class Fibbonacci:

    def __init__(self):
        self.log = {}

    def fibonacci(self, num):
        print(num)
        if num in [0, 1]:
            return 1

        if num in self.log:
            return self.log[num]
        self.log[num] = num * self.fibonacci(num - 1)

        return self.log[num]
