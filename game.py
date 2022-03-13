from sys import exit
def start():

    mc_hp = 100
    mc_attack = 20
    troll_hp = 100
    troll_attack = 5
    guardian_hp = 200
    guardian_attack = 25
    master_key = False
    flashlight = False
    medkit = False
    black_book = False

    print("""There are rumours of an abandoned house that
has hidden treasures inside, while looking for the house
you see a building appear out of nowhere.
Its small and only has 1 window and 1 door.
What will you do? """)

    while True:
        entry = input("\n> ")

        if entry == "enter door" or entry == "door" or entry == "open door":
            print("You open the door.")
            print("You are greeted by a butler.")
            print("He asks you to come in before knocking you out.")
            basement()

        elif entry == "open window" or entry ==  "window" or entry == "enter window":
            print("You enter through the window.")
            study()

        else:
            print("That's not going to work try something else.")



def study():
    print("You are in the study.")
    print("There is a desk, a bookshelf and a single door.")

    #print("<<< flashlight", repr(flashlight))
    #print("<<< black book", repr(black_book))


    while True:
        print("What will you do next?")
        #print("<<< flashlight", repr(flashlight))
        #print("<<< black book", repr(black_book))
        study = input("\n> ")

        if study == "investigate desk" or study == "desk" or study == "check desk":
            if flashlight:
                print("You have already checked this.")
            else:
                print("You walk over to the desk to check the draws.")
                print("One draw is locked and the other has a flashlight.")
                print("You take the flashlight")
                flashlight = True

        elif study == "investigate bookshelf" or study == "bookshelf" or study == "check bookshelf":
            if black_book:
                if master_key:
                    print("You open the bookshelf and use the master key to open the door.")
                    print("There is a set of stairs leading down into a dark room.")
                    print("Will you walk down the stairs?")
                    stairs = input(">")
                    if stairs == "yes":
                        dark_room()
                    else:
                        study()
                else:
                    print("The hidden door is still locked.")
            elif master_key:
                print("You walk over to the bookshelf and browse through the books.")
                print("You notice that there is a black book with no writing on the cover.")
                print("You pull on the book and realize its a switch, the bookshelf swings open to reveal a door.")
                print("The door is locked, you use the master key to open it.")
                print("There is a set of stairs leading down into a dark room.")
                print("Will you walk down the stairs?")
                stairs = input(">")
                if stairs == "yes":
                    dark_room()
                else:
                    study()

            else:

                print("You walk over to the bookshelf and browse through the books.")
                print("You notice that there is a black book with no writing on the cover.")
                print("You pull on the book and realize its a switch, the bookshelf swings open to reveal a door.")
                print("The door is locked, you close the bookshelf.")
                black_book = True

        elif study == "open door" or study == "door":
            if master_key:
                print("You can go to the kitchen, the bathroom or upstairs.")
                house = input(">")
                if house == "kitchen":
                    kitchen()
                elif house == "bathroom":
                    bathroom()
                elif house == "upstairs":
                    upstairs()
                else:
                    print("sorry you can't do that, you are back in the study.")
            else:
                print("You open the door to see a butler who says \"Its rude to trespass\", he knocks you out.")
                basement()
        else:
            print("Sorry you can't do that.")





































start()
