# #The Players
# players = ["Charlie", "Jason", "Derick", "Paul", "Simon"]

# #Slicing from the beginning of a list
# print(players[0:3])

# # Another way to slice from the beginning of a list
# print(players[:4])

# #Slicing the middle of a list
# print(players[2:4])

# #If you want to slice to the end of a list
# print(players[-4:])

#Looping through a slice using a for loop to loop through a subset of te elements within a list
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("Here are the two ice giants of our Solar System.")
for planet in planets[-2:]:
    print(planet.title())

print("The inner planets of our Solar System are")
for planet in planets[:4]:
    print(planet.title())