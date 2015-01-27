import random

with open("adjectives.txt") as f:
    adjectives = [i.strip() for i in f.readlines()]

with open("animals.txt") as f:
    animals = [i.strip() for i in f.readlines()]


def get_name():
    adjective = random.choice(adjectives)
    first_letter = adjective[0]
    animal = random.choice([i for i in animals if i[0] == first_letter])
    return "{} {}".format(adjective, animal)

for i in range(100):
    print get_name()

