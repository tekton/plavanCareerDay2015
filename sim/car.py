# The car from step 2
import random


class Car:
    wheels = 4
    color = "blue"
    min_spaces = 1
    max_spaces = 6
    total_moved = 0

    def __init__(self, *args, **kwargs):
        if "name" in kwargs:
            self.name = kwargs["name"]

    def move(self):
        spaces_moved = random.randint(self.min_spaces, self.max_spaces)
        self.total_moved += spaces_moved
        return spaces_moved

    def __str__(self):
        return "{}: has moved {} spaces".format(self.name, self.total_moved)
