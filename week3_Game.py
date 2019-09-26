# an object describing our player
import re
player = { 
    "name": "p1", 
    "items" : [],
    "location" : "start"
}


def sword():
    print "Do you want to pick it up?"
    pcmd = raw_input("please choose yes or no >")

    if (pcmd.lower() == "yes"):
        print "OH NO! You accidentally woke up the bear who's protecting the diamond!"
        pcmd = raw_input("Do you choose to run or fight?")
        
        if (pcmd.lower() =="run"):
            print "Sorry! You're not running fast enough because you're carrying the diamond and the sword. The bear caught you and you're dead."

        else: 
            print "Congratulations! Becuase you picked up the sword, you managed to beat the bear and got the diamond!"
            print "You're such a warrior! You can now gloriously walk back home and brag about your experience now!"
            raw_input("press enter >")
            print "to be continued..."


    else: 
        print "Sadly, you will be walking home with empty hands. Your boss might be angry and you could get fired :("
        print "But you got another opportunity!"
        raw_input("press enter >")
        sword()


def steak():
    pcmd = raw_input("Do you want to eat it or keep it?")

    if (pcmd.lower().strip()[0] == 'e'):
        print "Now you've enjoyed the wonderful meal, it's time to move forward..."
        raw_input("press enter >")
        print "You keep walking, but you got tripped by something..."
        raw_input("press enter >")
        print "There is a diamond by your feet! How lucky!"

        pcmd = raw_input("Do you want to pick it up?")

        if (pcmd.lower() == "yes"):
            print "OH NO! You accidentally woke up the bear who's protecting the diamond!"
            pcmd = raw_input("Do you choose to run or fight?")

            if (pcmd.lower() =="run"):
                print "Because you ate the steak, you run incredibly fast and you succesfully survived!"
                raw_input("press enter >")
                print "to be continued..."
            else: 
                print "Sorry, because you didn't pick up the sword before, you have no weapon and you're dead :( "
        
        else: 
            print "Sadly, you will be walking home with empty hands. Your boss might be angry and you could get fired :("
            
            raw_input("press enter >")
            print "to be continued..."
    
    else:
        print "Let's keep the meat in the bag and move forward..."
        raw_input("press enter >")
        print "You keep walking, but you got tripped by something..."
        raw_input("press enter >")
        print "There is a diamond by your feet! How lucky!"

        pcmd = raw_input("Do you want to pick it up?")

        if (pcmd.lower() == "yes"):
            print "OH NO! You accidentally woke up the bear who's protecting the diamond!"
            pcmd = raw_input("Do you choose to feed or fight?")

            if  (pcmd.lower() == "feed"):
                print "Because you kept the steak, you succesfully survived by running when he's eating the steak!"
                raw_input("press enter >")
                print "to be continued..."
            else: 
                print "Sorry, because you didn't pick up the sword before, you have no weapon and you're dead :( "
        
        else: 
            print "Sadly, you will be walking home with empty hands. Your boss might be angry and you could get fired :("
            
            raw_input("press enter >")
            print "to be continued..."
        


def InCave():
    print "Now you are in cave, you kept walking, and suddenly you see a sword and a steak!"
    print "Which one do you choose?"  
    pcmd = raw_input("Sword or steak?")

    if (pcmd.lower() == "sword"):
  
        print '          '
    	print '    11    '
    	print '   1111   '
    	print '   1111   '
    	print '   1111   '
    	print '   1111   '
        print '   1111   '
    	print '   1111   '
    	print '   1111   '
        print '   1111   '
    	print '   1111   '
    	print '   1111   '
    	print '   1111   '
    	print '   1111   '
    	print '   1111   '
    	print '11 1111 11'
    	print '1111111111'
    	print ' 11111111 '
        print '   1111   '
    	print '   1111   '
    	print '   1111   '
    	print '   1111   '
    	print '          '
    	print "You've got a sword! Let's move forward"

        raw_input("press enter >")
        print "You keep walking, but you got tripped by something..."
        raw_input("press enter >")
        print "There is a diamond by your feet! How lucky!"
        sword()

    elif (pcmd.lower() == 'steak'):
    	print "You've got a "

        print' ______   _________  ______   ________   ___   ___     '    
        print'/_____/\ /________/\/_____/\ /_______/\ /___/\/__/\    ' 
        print'\::::_\/_\__.::.__\/\::::_\/_\::: _  \ \\::.\ \\ \ \   '
        print' \:\/___/\  \::\ \   \:\/___/\\::(_)  \ \\:: \/_) \ \  '
        print'  \_::._\:\  \::\ \   \::___\/_\:: __  \ \\:. __  ( (  '
        print'    /____\:\  \::\ \   \:\____/\\:.\ \  \ \\: \ )  \ \ '
        print'    \_____\/   \__\/    \_____\/ \__\/\__\/ \__\/\__\/ '

        steak()

    else:
        print 'Sorry you may only choose one'
        InCave()


def introStory():
    print "Do you have the courage to explore the cave?"
    pcmd = raw_input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print "Great! A miner should be very risk-taking..."
        raw_input("press enter >")
        InCave()
    else:
        print "Sorry, you'll starve to death if you don't go"
        pcmd = raw_input("press enter >")
        introStory() # repeat over and over until the player chooses yes!


 # let's introduce them to our world
print "What should I call you?"
player["name"] = raw_input("Please enter your name >")

# intro story, quick and dirty (think star wars style)
print '                _____        ______  _    _     ______      _    _ _______ '
print '               (____ \   /\ (_____ \| |  / )   / _____)  /\| |  | (_______)'
print '                _   \ \ /  \ _____) ) | / /   | /       /  \ |  | |_____   '
print '               | |   | / /\ (_____ (| |< <    | |      / /\ \ \/ /|  ___)  '  
print '               | |__/ / |__| |    | | | \ \   | \_____| |__| \  / | |_____ ' 
print 'Welcome to the |_____/|______|    |_|_|  \_)   \______)______|\/  |_______)' + " " + player["name"] + "!"
                                                            

print "You're an experienced miner, and you just discovered a myeterious new cave..."
print "It is pitch dark in the front, and your flashlight is about to run out..."
#print "Do you dare to explore the cave?"
introStory()






