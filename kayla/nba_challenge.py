# print("Challenge 2.1:")

jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
fred_VanVleet_3pts_made = 43
# TODO: Create variable here for number of 3 pt shots made by James Harden
james_harden_3pts_made = 47


# print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
# # TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {fred_VanVleet_3pts_made} 3 point shots")
# # TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")

# print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# # TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
# # TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
# # TODO: Create variable here for number of 3 pt shot attempts by James Harden
# print("challenge 2.4")
james_harden_3pts_attempt = 93
fred_VanVleet_3pts_attempt = 110
jamal_murray_3pts_attempt = 109
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots shots and atttempted {jamal_murray_3pts_attempt}")
# # TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {fred_VanVleet_3pts_made} 3 point shots shots and atttempted {fred_VanVleet_3pts_attempt}")
# # TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots and atttempted {james_harden_3pts_attempt}")


print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
jamal_murray_3pts_total = jamal_murray_3pts_attempt + jamal_murray_3pts_made
jamal_percentage =  float(jamal_murray_3pts_made)/float(jamal_murray_3pts_attempt)
print(jamal_percentage)
# TODO: Calculate and print the 3 point percentage for Fred VanVleet

fred_VanVleet_3pts_total = (
    fred_VanVleet_3pts_attempt + fred_VanVleet_3pts_made)
fred_percentage = float(fred_VanVleet_3pts_made)/float(fred_VanVleet_3pts_attempt) 

# TODO: Calculate and print the 3 point percentage for James Harden
james_harden_3pts_total = (james_harden_3pts_attempt + james_harden_3pts_made)

james_percentage = float(james_harden_3pts_made) / float(james_harden_3pts_attempt)


# # print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
sentence = '''The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. 
\n They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. 
\n Those three have made good developments with the Pelicans, especially Brandon Ingram. 
\ But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. 
\n Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. 
\n The Lakers ended the season atop the Western Conference with a record of 49-14. 
\n They were narrowly behind the Bucks for the best record in the league. 
\n Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. 
\n Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.'''
print(sentence)

# # print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# # # TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case
print(sentence.upper())

# # print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# # # TODO: make a variable called `lakers_are_best` to indicate this
lakers_are_best = False
# # # TODO: print out the variable in an f-string to convey your opinion on the lakers
if lakers_are_best == False:
    opinion = "NOT"
else:
    opinion = "DEFINITELY"

print(f"lakers are {opinion} the best")

# # print('Challenge 3.4: Type Conversion')
# # # TODO: Convert your `lakers_are_best` variable to an integer, and print it out.
new_lakers_var = int(lakers_are_best)
print(new_lakers_var)
# # # TODO: Convert your `lakers_are best` variable to a float, and print it out
newest_lakers_var = float(new_lakers_var)
print(newest_lakers_var)
# # print('Challenge 3.5: Type Conversion Part 2')
# # # TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
jamal_percentage_to_str = str(jamal_percentage)
print(type(jamal_percentage_to_str), jamal_percentage_to_str) 
james_percentage_to_str = str(james_percentage)
print(type(james_percentage_to_str),james_percentage_to_str)
fred_percentage_to_str = str(fred_percentage)
print(type(fred_percentage_to_str),fred_percentage_to_str)
# # # TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
jamal_to_int = int(jamal_percentage)
print(type(jamal_to_int), jamal_to_int)
james_to_int = int(james_percentage)
print(type(james_to_int), james_to_int)
fred_to_int = int(fred_percentage)
print(type(fred_to_int), fred_to_int)
