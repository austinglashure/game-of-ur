import random


class Dice:
    def __init__(self):
        self.roll = []  # need to put 4 die objects
        for i in range(4):
            self.die = [0, 1, 0, 1]  # creates die object
            self.roll.append(self.die)  # appends it to roll object

    def get_roll_score(self):
        score = 0
        for foo in self.roll:  # iterates through die objects in roll object
            bar = random.sample(foo, 1)  # sample returns list with one item
            score += bar[0]  # adds the die value to the score
        return score


dice = Dice()
