import random
class Dice:
    def roll(self):
        numbers=(1,2,3,4,5,6)
        for number in numbers:
            random1=random.choice(numbers)
            random2=random.choice(numbers)
        print((random1,random2))


dice=Dice()
dice.roll()

