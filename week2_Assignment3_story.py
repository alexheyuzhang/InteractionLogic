# let the user know what's going on
print ("Welcome to MadLib   s!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
number1= raw_input("Enter your favorite number: ")
location1 = raw_input("Name a place you want to go: ")
character1 = raw_input("enter a celebrity's name:")
adjective1 = raw_input("Enter an adjective: ")
color1 = raw_input("What is your favorite color?: ")
animal1 = raw_input("Enter your favorite animal: ")
food1 = raw_input("Enter what you ate for your last meal: ")


# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!


#Once a upon a time, there were 7 princesses trapped in a tiny house in the dark forest by an evil dwarf. 
#One day, however, a rabbit carrying a bag of carrots got lost in the forest and found the princesses. 
#In order to save the princess, the nice rabbit poisoned the dwarf with the carrots he brought. 
#The 7 princesses then lived with the rabbit happyily ever after. 


story = ("Once upon a time, there were " + number1 + " princesses trapped in a tiny cave in " + location1 +\
" by a " + adjective1 + " " + character1 + ". One day, however, a " + animal1 + " carrying a bag of " 
+ food1 + " got lost in the " + location1 + " and found the princesses. In order to save them, the " +\
animal1 + " poisoned the " + character1 + " with the " + food1 + " he brought with him. Then the " + animal1+\
" and princesses lived happily ever after.")



# finally we print the story
print (story)