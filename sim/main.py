from car import Car
from track import RaceTrack

import random


# create a basic, empty game
class Game(object):
    cars = []
    track = None
    winner = None
    stage = 0
    sim_active = False

    def __init__(self, *args, **kwargs):
        if "name" in kwargs:
            self.name = kwargs["name"]
        else:
            self.generate_name()

        if "cars" in kwargs:
            self.cars = kwargs["cars"]

        if "track" in kwargs:
            self.track = kwargs["track"]
        else:
            self.track = RaceTrack()

    def generate_name(self):
        self.name = "Game {0:06d}".format(random.randint(1, 1000000))

    def check_winner(self, car):
        if car.total_moved >= self.track.spaces:
            self.winner = car
            return True
        else:
            return False

    def next_round(self):
        '''
            Go through the players, furthest first, and move them forward
        '''
        self.stage += 1
        self.cars = sorted(self.cars, key=lambda car: car.total_moved)
        for car in self.cars:
            car.move()
            if self.check_winner(car):
                return True
            else:
                pass
                # print("{} moved to space {}.".format(car.name, car.total_moved))
        return False

    def reset_cars(self):
        for car in self.cars:
            car.total_moved = 0

    def run_sim(self):
        if self.sim_active:
            print("There's already a sim running, please wait")
            return
        self.sim_active = True
        self.stage = 0
        self.winner = None
        if not self.name:
            self.generate_name()
        while self.stage < self.track.max_rounds:
            if self.winner:
                break
            self.next_round()
        if self.winner:
            print("Winner was {} in {} rounds.".format(self.winner, self.stage))
        else:
            self.cars = sorted(self.cars, key=lambda car: car.total_moved)
            print("{1} :: No one got to the finish line in time, furthest moved: {0}".format(self.cars[len(self.cars)-1],  # noqa
                                                                                             self.name))
        self.sim_active = False
        self.reset_cars()
        self.name = None


def __main__():
    print("Attempting simulation of car game with 4 players.")
    car_one = Car(name="Player One")
    car_two = Car(name="Player Two")
    car_three = Car(name="Player Three")
    car_four = Car(name="Player Four")

    cars = [car_one, car_two, car_three, car_four]

    game = Game(cars=cars)
    game.run_sim()

    for x in range(0, 100):
        game.run_sim()


__main__()
