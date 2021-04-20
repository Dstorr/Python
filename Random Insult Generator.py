import random

#Random Insult Generator
print("Random Insult Generator")

#Arrays 
insults = ["You look disgusting", "You are terrible", "You are a mean creature", "Get a better design next time", "You need to lose weigh", "You are not funny"]

animals = ["Horse.", "Dog.", "Cat.", "Elephant.", "Platypus.", "Rat.", "Tiger.", "Bear.", "Rabbit.", "Rhino."]

#Random number 
rand_insult = random.randint(0,len(insults)-1)
rand_animal = random.randint(0,len(animals)-1)

#Output 
print(insults[rand_insult], animals[rand_animal])