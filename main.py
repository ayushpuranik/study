"""from greetings import Greetings

name = input("What is your name? ")
year = int(input("In which year you were born? "))

from agecalculator.AgeCalculator import AgeCalculator

ac = AgeCalculator()


print(f'{Greetings.sayHello(name)} You are {ac.getAge(year)} years old')
"""

# from fib.Fibbonacci import Fibbonacci as fb
# fb = fb()
# print(fb.fibonacci(6))

# from prime import Prime
# 
# for i in range(1,50):
#     print(i, Prime.isPrime(i))

# from pelindrome import Pelindrome
#
# print(Pelindrome.getPelindrome("Ayush"))


num = 434566


def getIntPelindrome(num):
    digits = []
    temp = num
    while temp != 0:
        digits.append(temp % 10)
        temp = temp // 10
    res = 0
    for i in digits:
        res = res * 10 + i
    return res

for i in range(1,10000):
    print(getIntPelindrome(i))
