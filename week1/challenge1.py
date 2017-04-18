# Why you should take this OM course

import random

# Cards
courses = ["One Month Python",
        "One Month Python",
        "One Month Rails",
        "One Month Project Management",
        "One Month iOS",
        "One Month Product Development"]

# Our list of friends
reasons = ["get a hot date tomorrow",
    "show your kindergarten teacher you can be an astronaught",
    "finally make dad proud of you",
    "learn a cool skill",
    "never watch the videos and blow two hundred dollars",
    "achieve personal growth in that area"]

random_course = random.choice(courses)
random_reason_one = random.choice(reasons)
random_reason_two = random.choice(reasons)
while random_reason_two == random_reason_one:
    random_reason_two = random.choice(reasons)
    if random_reason_two != random_reason_one:
        break

print("You should take %s if you want to %s or if you want to %s." % (random_course, random_reason_one, random_reason_two))

list = ['* *', '*', '* * *', '* * * * *', '* * * * * *', '* * * *']
for i in list:
    print i
