import datetime

class AgeCalculator:
    def __init__(self):
        pass

    def getAge(self, yearOfBirth):
        year = datetime.date.today().year
        return  (year - yearOfBirth) if (year - yearOfBirth) >= 0 else -1
