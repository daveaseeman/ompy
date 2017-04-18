# What Should I Do Tonight?

import random

# Our list of bars
bars = ["Lion's Head Tavern",
        "The Hamilton",
        "1020 Bar",
        "Amsterdam Tavern",
        "The Heights",
        "The Dead Poet",
        "Prohibition",
        "302",
        "Whiskey Kitchen"]

# Our list of friends
people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Alexander Hamilton",
          "Samuel L. Jackson",
          "Kanye West",
          "Seth Godin",
          "Barrack Obama"]

random_bar = random.choice(bars)
random_person_one = random.choice(people)
random_person_two = random.choice(people)
while random_person_two == random_person_one:
    random_person_two = random.choice(people)
    if random_person_two != random_person_one:
        break

print("How about you go to %s with %s and %s?" % (random_bar, random_person_one, random_person_two))
