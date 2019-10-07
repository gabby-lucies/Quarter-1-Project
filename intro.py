#importing
import time

#How players could respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Objects
fwomp = 0
bownarrow = 0
sword = 0
money = 0

#playerName = input("Enter Your Name: ") #gets the player's name, obviously
required = ("\nUse only A, B, or C.\n")

#Startup
def intro():
    #print("There is no saving. Sorry!")
    #print("Hello! Please enter your name.")
    #print("Nice to meet you!")
    print("Let's begin!")
    print("You wake up in a forest. You can't remember anything. You look around and find")
    print("a small creek. You hear sound nearby that sounds like some sort of woodland creature.")
    print("You also see some smoke in the distance. What would you like to do ?")
    time.sleep(2)
    #Choice 1 Options
    print("A. Follow the creek.")
    print("B. Follow the sound of the woodland creature.")
    print("C. Walk towards the smoke.")
    choice = input(">>> ") #gets choice
    time.sleep(1.5)
    if choice in answer_A:
        option_creek() #Gives player creek option
    elif choice in answer_B:
        option_animal() #Give Fwomp options
    elif choice in answer_C:
        option_smoke() #Gives smoke options
    else:
        print(required)
        intro()

def option_creek():
    print("You follow the creek for an hour, and you eventually come across the river.")
    print("You followed the river for another hour, and you found a riverside village.")
    print("You walk into the village, desperately looking for food and water.")
    print("You come across a large pub. It doesn't look very busy.")
    print("You also come across an elegant resturant. It must be very expensive.")
    print("There is also family outside of their house eating freshly picked food from their garden.")
    print("Where will you go?")
    print("A. Pub B. Resturant C. Family")
    time.sleep(2.5)
    choice = input(">>> ")
    if choice in answer_A:
        option_pub()
    if choice in answer_B:
        option_resturant()
    if choice in answer_C:
        option_family()
    else:
        print(required)
        option_creek()

def option_smoke():
    print("You walk towards the smoke. Eventually you find the source of the smoke.")
    print("The smoke is coming from a lost and very angry tribe.")
    print("They also don't speak your language.")
    print("When they spot you, and you have nothing to offer them in return, so they assume you are there to kill them.")
    print("Anways, fifty of them shot you with arrows all at once.")
    time.sleep(2)
    print("Also, you're dead!")
    time.sleep(2)
    option_smoke()


def option_animal():
    print("Seriously, you walked towards a strange animal sound just like that?")
    print("Luckily, it is only a Fwomp. It doesn't kill you, but it does glare at you strangely.")
    print("Fwomps are cute, so you want to pet it.")
    print("You also want to take the Fwomp.")
    print("You're also hungry and horrible so you also kind of want to eat the Fwomp.")
    print("What will you do?")
    print("A. Pet Fwomp B. Take Fwomp C. Eat Fwomp") 
    time.sleep(2.5)
    choice = input(">>> ")
    if choice in answer_A:
        fwomp = 1
        option_petfwomp()
    elif choice in answer_B:
        fwomp = 1
        option_takefwomp()
    elif choice in answer_C:
        option_eatfwomp()
    else:
        print(required)
option_animal()

def option_petfwomp():
    print("The Fwomp likes you. It is now following you.")
    print("YOU NOW HAVE fwomp IN YOUR INVENTORY!")
    print("The fwomp is very loyal, she may be useful to you later")
    print("Where should you go next?")
    print("You can either follow the creek or follow the smoke.")
    print("Y. Creek N. Smoke")
    time.sleep(2.5)
    choice = input(">>> ")
    if choice in yes:
        option_creek()
    if choice in no:
        option_smoke()
    else:
        print(required)
option_petfwomp()

def option_takefwomp():
    print("You take the fwomp without its consent. You are horrible")
    print("Fortunately, the fwomp is friendly and doesn't seem to care.")
    print("YOU NOW HAVE A fwomp IN YOUR INVENTORY!")
    print("The fwomp is very loyal, she may be useful to you later")
    print("Where should you go next?")
    print("You can either follow the creek or follow the smoke.")
    print("Y. Creek N. Smoke")
    time.sleep(2.5)
    choice = input(">>> ")
    if choice in yes:
        option_creek()
    if choice in no:
        option_smoke()
    else:
        print(required)
option_takefwomp()
    
def option_eatfwomp():
    print("You snap the fwomp's throat, and feel the innocent creature go limb in your hands")
    print("You devour the fwomp, without cooking it.")
    print("You also forgot that fwomps, if not cooked right, are extremely toxic to hoomans.")
    print("You're dead, but you deserved it.")
    print("Try again by exiting.")
    time.sleep(2.5)
option_eatfwomp()

def option_resturant():
    print("You walk into the resturant to get some din dins.")
    print("You order some food to eat.")
    print("After the meal the waiter comes to you for your check.")
    print("However, you don't have money.")
    print("The waiter gives you two options:")
    print("Y: Take this to the police")
    print("N: Help him in exchange for money.")
    print("Which will you choose?")
    time.sleep(2.5)
    choice = input(">>> ")
    if choice in yes:
        print("The police of the village choose to execute you.")
        print("You're dead, try again!")
        time.sleep(2) 
        exit()   
    if choice in no:
        print("The waiter gives you the task of finding a lost scientist.")
        print("He went missing in the Rosach Mountains.")
        print("You travel there quickly, looking for the mad scientist.")
        print("You search the dangerous, rigid mountains for hours and hours.")
        time.sleep(2) #Pauses sequence of events for 2 seconds
        print("You finally find the scientist in a cave.")
        print("Do you want to approach cautiously, or kidnap him?")
        print("Y: Kidnap N: Approach cafefully")
        choice = input(">>>" )
        if choice in yes:
            print("The mad scientist feels endangered by you.")
            print("He quickly grabs a mysterious chemical and spashes it on you.")
            print("It burns the flesh of your bones in moments.")
            print("You're dead!")
            time.sleep(2)
            exit()
        if choice in no:
            print("You approach the mad scientist cautiously.")
            print("He looks over at you and asks who you are.")
            print("You introduce yourself")
            print("You inform him that you came here to take him back to the village.")
            print("The scientist agrees to come with you.")
            print("He explains he came here to do some experiments,")
            print("however, he got lost and couldn't find his way back.")
            print("You travel back to the village, and to the waiter.")
            print("The waiter does as he promised and waived your bill.")
            time.sleep(5)
option_resturant()

def option_family():
    print("You approach the family")
    print("The little girl screams loudly, and runs to her father.")
    print("The father comes out of the house with an axe, and comes after you.")
    print("You tried to outrun him, but he was much faster than you.")
    print("He decapitates you.")
    print("You're dead, obviously")
    time.sleep(3)
    exit()
option_family()

def option_pub():
    print("You walk in and look horrible. Luckily, the people here are very kind.")
    print("They clean you up and give you a free meal.")
    print("While in there, a woman who knows the owner asks if you have seen some elves.")
    print("You tell her you haven't. She proceeds to talk about the elves for an hour.")
    print("The elves keep harassing her and her family.")
    print("Although they said the meal was on the house, she tries using the free meal against you.")
    print("It works, and you leave to take care of the situation.")
    print("You find the elves in the forest you came from. You need to find a way to deal with them.")
    print("Will you kill all of them, or try and settle things peacefully?")
    print("Y. Violence! N. Peace")
    time.sleep(3.5)
    choice = input(">>> ")
    if choice in yes:
        print("The elves are very strong, even though they are three feet tall.")
        print("They brutally eat your face off like a Florida man on bathsalts.")
        print( "Oh, and you're obviously dead. Try again!")
    elif choice in no:
        print("You fixed the situation with the elves! They agree to stop harassing the woman and her family.")
    else:
        print(required)
option_pub()