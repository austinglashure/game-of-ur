import random
import pygame


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


red = (250, 0, 0)
green = (0, 250, 0)
blue = (0, 0, 250)
white = (250, 250, 250)
black = (0, 0, 0)
# the basic colors to illustrate things
pygame.init()  # activates the pygame module
dims = (800, 800)
window = pygame.display.set_mode(dims)  # created window object with the dimensions
pygame.display.set_caption("Ur EEE Tarded")  # self motivation
clock = pygame.time.Clock()  # created clock object to set frame rate
dice = Dice()  # created dice object to get dice rolls for the game


on = True  # will be the boolean to flip and kill the program loop
while on:  # basic pygame loop
    window.fill(white)  # just so it isn't black
    pygame.display.flip()  # refreshes the display rendering
    for e in pygame.event.get():  # everything is triggered by events
        if e.type == pygame.QUIT:  # pygame's built in QUIT will trigger if the X is clicked
            on = False  # kill the program loop
        elif e.type == pygame.KEYDOWN:  # to detect a key stroke
            if e.key == pygame.K_ESCAPE:  # another way to kill the program
                on = False  # kill it

    clock.tick(60)  # sets the frame rate at 60 seconds

