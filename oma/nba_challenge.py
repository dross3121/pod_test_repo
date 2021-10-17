print ("Challenge 2.1: Store the number of three point shots made in variables for each player\n\n")
#create variables to track the number of 3-point shots Fred VanVleet and James Harden have made.

jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

print ("jamal_murray_3pts_made = 46")
print("fred_vanvleet_3pts_made = 43")
print("james_harden_3pts_made = 37\n\n")

print("Challenge 2.2: Print out the number of three point shots using f-strings with the variables \
    created for each player in 2.1\n\n")

print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made}, 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made}, 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made}, 3 point shots\n\n") 

print ("Challenge 2.3: Store the number of three point shot attempts in variables for each player.\n")
jamal_murray_3pts_attempts = 93
fred_vanvleet_3pts_attempts = 110
james_harden_3pts_attempts = 109

print("jamal_murray_3pts_attempts = 93")
print("fred_vanvleet_3pts_attempts = 110")
print("james_harden_3pts_attempts = 109\n\n")

print("Challenge 2.4: Build on your print statement!\n\n")
print(f"In the 2020 NBA playoffs, Jamal Murray attempted {jamal_murray_3pts_attempts}, & made {jamal_murray_3pts_made}, 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet attempted {fred_vanvleet_3pts_attempts}, & made {fred_vanvleet_3pts_made}, 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden attempted {james_harden_3pts_attempts}, & made {james_harden_3pts_made}, 3 point shots\n\n")

print("Challenge 2.5: Calculate and print the three point percentage for each player.")
#The three point percentage is given by the following formula: 3 point shots made/3 point shots attempted

jamal_three_point_percentage = jamal_murray_3pts_made/jamal_murray_3pts_attempts
fred_three_point_percentage = fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempts
james_three_point_percentage = james_harden_3pts_made/james_harden_3pts_attempts

print(f"Jamal Murray 3 Point Percentage in the 2020 NBA playoffs were,  {jamal_three_point_percentage} %")
print(f"Fred VanVleet 3 Point Percentage in the 2020 NBA playoffs were,  {fred_three_point_percentage} %")
print(f"James Harden 3 Point Percentage in the 2020 NBA playoffs were,  {james_three_point_percentage} %\n\n")

print("Challenge 3: Formatting string information about the Lakers\n")
#Challenge 3: Formatting string information about the Lakers

print("Challenge 3.1 Print out the paragraph but with only 1 sentence per line\n")

print("Challenge 3.2 Print out the paragraph with only 1 sentence per line, and all in upper case\n")

print ("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\
They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\
Those three have made good developments with the Pelicans, especially Brandon Ingram.\
But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\
Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\
The Lakers ended the season atop the Western Conference with a record of 49-14.\
They were narrowly behind the Bucks for the best record in the league.\
Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\
Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.\n\n".upper)

print("Challenge 3.3 Are the Lakers the best team?\n")
#Make a boolean variable called lakers_are_best that indicates, to the best of your knowledge, 
#  whether the following statement is true: The Lakers are the best basketball team in the NBA
#Using an f-string containing your lakers_are_best variable, print out your evaluation of 
#  whether the statement was true or not
print("Make a boolean variable called 'lakers_are_best', & print out your\
    evaluation of whether the statement was true or not \n")

a = True
b = False
lakers_are_best = False

print (f"{lakers_are_best}\n\n")

print ("Challenge 3.4 Type conversion")
#Challenge 3.4 Type conversion
print ("Convert your lakers_are_best variable to an integer, and print it out.")
print ("Curent Variable Type")
print (f"lakers_are_best: {type(lakers_are_best)}\n")
bool = lakers_are_best
print (int(lakers_are_best))