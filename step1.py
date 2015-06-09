# Basics of randomization
'''
    One of the things that makes games replayable is the pseudo-random nature
    of random numbers- in physical games that's easily done with dice.
'''
import random

# How many sides on the dice do we want? 6, 8, 10, 12, 20 and 100 are normal
SIDES = 6

# We want a random intenger, meaning only full round numbers
x = random.randint(1, SIDES)

# Lets print out what we got!
print(x)

# What happens when we do it a lot?
for x in range(1, 101):
    print(x, str(random.randint(1, SIDES)))
