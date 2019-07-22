import time


import random


weapons = ["tomahawk", "lance", "Sword"]
value = random.choice(weapons)

def print_pause(message):
    print(message)
    time.sleep(2)



def field():  

    print_pause("You find yourself standing in an open field\n" 
                "filled with grass and yellow wildflowers.")
    print_pause("rumor has it that a wicked fairie\n"
                "is somewhere around here\n" 
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold\n"
                "your trusty (but not very effective) dagger.")
def house(value):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock"
                "when the door opens and out steps a wicked fairie.")
    print_pause("Eep! This is the wicked fairie's house!")
    print_pause("The wicked fairie attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                "what with only having a tiny dagger.")
    option = input("Would you like to (1) fight or (2) run away?")
    if option == 1:
        if "tomahawk" in value:
            print_pause("As the wicked fairie moves to attack"
                        "you unsheath your new sword.")
            print_pause("The'tomahawk'shines brightly in your hand"
                        "as you brace yourself for the attack.")
            print_pause("But the wicked fairie takes one look"
                        "at your shiny new toy and runs away!")
            print_pause("You have rid the town of the wicked fairie."
                        "You are victorious!")

        else:
            print_pause("You do your best...")
            print_pause("but your dagger"
                        "is no match for the wicked fairie.")
            print_pause("You have been defeated!")
        if "lance" in value:
            print_pause("As the wicked fairie moves to attack"
                            "you unsheath your new sword.")
            print_pause("The'lance'shines brightly in your hand"
                            "as you brace yourself for the attack.")
            print_pause("But the wicked fairie takes one look"
                            "at your shiny new toy and runs away!")
            print_pause("You have rid the town of the wicked fairie."
                            "You are victorious!")

        else:
            print_pause("You do your best...")
            print_pause("but your dagger"
                            "is no match for the wicked fairie.")
            print_pause("You have been defeated!")
        if "Sword" in value:
                print_pause("As the wicked fairie moves to attack"
                                "you unsheath your new sword.")
                print_pause("The Sword'shines brightly in your hand"
                                "as you brace yourself for the attack.")
                print_pause("But the wicked fairie takes one look"
                                "at your shiny new toy and runs away!")
                print_pause("You have rid the town of the wicked fairie."
                                "You are victorious!")
        else:  
                print_pause("You do your best...")
                print_pause("but your dagger"
                                "is no match for the wicked fairie.")
                print_pause("You have been defeated!")
                
    elif option == 2:
        print_pause("You run back into the field."
                    "Luckily, you don't seem \n"
                    "to have been followed.") 
        adventure(value)
        
def cave(value):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")  
    print("You have found the magical", value)
    print("You discard your silly old dagger"
          "and take the", value, "with you.")
    print_pause("You walk back out to the field.")
    adventure(value)


def adventure(value):                      
    choice = input("Enter 1 to knock on the door of the house.\n"
                   "Enter 2 to peer into the cave.\n"
                   "What would you like to do?\n"
                   "(Please enter 1 or 2.)").lower()
    if choice == 1:
        house(value)
    elif choice == 2:
        cave(value)




def start_game():
    field()
    adventure(value)     

start_game()

while True:
    pa = input("Would you like to play again? (y/n)").lower()
    if pa == "n":
        print_pause("Thanks for playing! See you next time.")
        break
    elif pa == "y":
        
        print_pause("Excellent! Restarting the game ...")
        start_game()
