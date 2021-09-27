print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
vanvleet_3pts_made = 43
# TODO: Create variable here for number of 3 pt shots made by James Harden
harden_3pts_made = 37

print("Challenge 2.2:")

# TODO: Create print statement here for Fred VanVleet
# TODO: Create print statement here for James Harden

print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {harden_3pts_made} 3 point shots")


print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")

jamal_murray_3pt_attempts = int(46/3)
vanvleet_3pt_attempts = int(43/3)
harden_3pt_attempts = int(37/3)


# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
# TODO: Create variable here for number of 3 pt shot attempts by James Harden

print(f"Jamal Murray had {jamal_murray_3pt_attempts} shot attemps to score {jamal_murray_3pts_made} points.")
print(f"Fred Vanvleet had {vanvleet_3pt_attempts} shot attemps to score {vanvleet_3pts_made} points.")
print(f"James Harden had {harden_3pt_attempts} shot attemps to score {harden_3pts_made} points.")



print()

# print("Challenge 2.4: Build on your print statement")
# # TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# # the number of three point shots for each player. E.g., output should be similar to
# # "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
# print()


print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {jamal_murray_3pt_attempts} shot attemps to score 46 points. ")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {vanvleet_3pts_made} 3 point shots from {vanvleet_3pt_attempts} shot attempts." ) 
print(f"In the 2020 NBA playoffs, James Harden made {harden_3pts_made} 3 point shots from {harden_3pt_attempts} shot attempts.")


# print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# # TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# # TODO: Calculate and print the 3 point percentage for Jamal Murray
# # TODO: Calculate and print the 3 point percentage for Fred VanVleet
# # TODO: Calculate and print the 3 point percentage for James Harden
# print()

jamal_murray_3pt_percentage = round((15/46) * 100)
print(f"Jamal Murray's 2020 3pt playoff percentage is {jamal_murray_3pt_percentage} percent.")

vanvleet_3pt_percentage = round((14/43) * 100)
print(f"Fred Vanvleet's 2020 3pt playoff percentage is {vanvleet_3pt_percentage} percent.")

harden_3pt_percentage = round((12/37) * 100)
print(f"Jame Harden's 2020 3pt playoff percentage is {harden_3pt_percentage} percent.")



jamal_murray_3pt_percentage = round((15/46) * 100)
print(f"Jamal Murray's 2020 3pt playoff percentage \nis {jamal_murray_3pt_percentage} percent.")

vanvleet_3pt_percentage = round((14/43) * 100)
print(f"Fred Vanvleet's 2020 3pt playoff percentage \nis {vanvleet_3pt_percentage} percent.")

harden_3pt_percentage = round((12/37) * 100)
print(f"Jame Harden's 2020 3pt playoff \npercentage is {harden_3pt_percentage} percent.")


# print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# # TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line

# print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# # TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case


jamal_murray_3pt_percentage = round((15/46) * 100)
print(f"Jamal Murray's 2020 3pt playoff percentage is {jamal_murray_3pt_percentage} percent.".upper())

vanvleet_3pt_percentage = round((14/43) * 100)
print(f"Fred Vanvleet's 2020 3pt playoff percentage is {vanvleet_3pt_percentage} percent.")

harden_3pt_percentage = round((12/37) * 100)
print(f"Jame Harden's 2020 3pt playoff percentage is {harden_3pt_percentage} percent.")


# print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# # TODO: make a variable called `lakers_are_best` to indicate this
# # TODO: print out the variable in an f-string to convey your opinion on the lakers

lakers_are_the_best = True
print(f"That the Lakers are the best team in the NBA after the Knicks is {lakers_are_the_best}")

# print('Challenge 3.4: Type Conversion')
# # TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
lakers_are_the_best = int(True)
print(lakers_are_the_best)

# # TODO: Convert your `lakers_are best` variable to a float, and print it out

lakers_are_the_best = float(True)
print(lakers_are_the_best)

# print('Challenge 3.5: Type Conversion Part 2')
# # TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
# # TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.

jamal_murray_3pt_percentage = str(round((15/46) * 100))
print(jamal_murray_3pt_percentage)
print(type(jamal_murray_3pt_percentage))

jamal_murray_3pt_percentage = int(round((15/46) * 100))
print(jamal_murray_3pt_percentage)
print(type(jamal_murray_3pt_percentage))


vanvleet_3pt_percentage = str(round((14/43) * 100))
print(vanvleet_3pt_percentage)
print(type(vanvleet_3pt_percentage))

vanvleet_3pt_percentage = int(round((14/43) * 100))
print(vanvleet_3pt_percentage)
print(type(vanvleet_3pt_percentage))


harden_3pt_percentage = str(round((12/37) * 100))
print(harden_3pt_percentage)
print(type(harden_3pt_percentage))

harden_3pt_percentage = int(round((12/37) * 100))
print(harden_3pt_percentage)
print(type(harden_3pt_percentage))


