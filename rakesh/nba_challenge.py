print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37
print()

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")
print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_attempts = 93
fred_vanvleet_3pts_attempts = 110
james_harden_3pts_attempts = 109
print()

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3-point shots out of {jamal_murray_3pts_attempts} attempts.")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3-point shots out of {fred_vanvleet_3pts_attempts} attempts.")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3-point shots out of {james_harden_3pts_attempts} attempts.")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
print(f"Jamal Murray's 3-point percentage was {round((jamal_murray_3pts_made/jamal_murray_3pts_attempts)*100,2)}%.")
print(f"Fred VanVleet's 3-point percentage was {round((fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempts)*100,2)}%.")
print(f"James Harden's 3-point percentage was {round((james_harden_3pts_made/james_harden_3pts_attempts)*100,2)}%.")
print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\
    \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\
    \nThose three have made good developments with the Pelicans, especially Brandon Ingram.\
    \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\
    \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\
    \nThe Lakers ended the season atop the Western Conference with a record of 49-14.\
    \nThey were narrowly behind the Bucks for the best record in the league.\
    \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\
    \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.")
print()

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\
    \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\
    \nThose three have made good developments with the Pelicans, especially Brandon Ingram.\
    \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\
    \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\
    \nThe Lakers ended the season atop the Western Conference with a record of 49-14.\
    \nThey were narrowly behind the Bucks for the best record in the league.\
    \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\
    \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.".upper())
print()

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
lakers_are_best = False
print(f"The Lakers the best team in the NBA. {lakers_are_best}")
print()

print('Challenge 3.4: Type Conversion')
print (int(lakers_are_best)) #it takes a value of 0 because False=0 in Boolean.
print (float(lakers_are_best))
print()

print('Challenge 3.5: Type Conversion Part 2')
#  3-point percentage to str
print("3-point percentages as strings:")
jamals_3point_percentage = jamal_murray_3pts_made/jamal_murray_3pts_attempts
print (str(jamals_3point_percentage),"%") #percentage doesn't change it is converted to a string
freds_3point_percentage = fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempts
print (str(freds_3point_percentage),"%")
james_3point_percentage = james_harden_3pts_made/james_harden_3pts_attempts
print (str(james_3point_percentage),"%")
print()

# 3-point percentage to integer
print("3-point percentages as integers (%):")
print (int(jamals_3point_percentage)) #decimal percentages are truncated
print (int(freds_3point_percentage))
print (int(james_3point_percentage))
print()
