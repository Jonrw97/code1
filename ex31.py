print("""You enter a dark room with two doors.
Do you walk through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a strange man standing alone.")
    print("What do you do?")
    print("1. Say Hi.")
    print("2. Ignore him and search the room.")

    room = input("> ")

    if room == "1":
        print("The man says hi back.")
        print("He asks for your name.")
        print("Will you tell it to him?")
        answer = input("Y/N  >")

        if answer == "Y":
            name = input("Insert name here >")
            print(f"""The man says thank you and then disappears, you slowly fade from exsitance.
            Now you know don't give your name to strange people, {name}.""")
        elif answer == "N":
            print("The man smiles and says \"well done you shouldnt just hand out your name to strange people.\"")
            print("He diappears and a door opens behind him and you leave. Well done!")
        else :
            print("The man screams and attacks you, you died. Oh well.")

    elif room == "2":
        print("The man stands still as you look around the room you notice a cord hanging from the ceiling.")
        print("Do you pull the cord?")

        answer = input("Y/N  >")
        if answer == "Y":
                print("A blinding white light appears and you cease to exist. Oh well.")
        elif answer == "N":
                print("The man says \"well done\" and dissappears a door appears where he stood")
                print("You exit through the door and go home. Well done")

    else:
        print("After stand around doing {room} the man screams and attacks you.")
        print("You died, oh well.")

elif door == "2":
    print("You open the door and fall down an endless pit.")
    print("You have 2 options accept that you will fall foever or do something.")

    do = input("What will you do > ")

    if do == "accept":
        print("You accept that you will fall for all eternity and you eventaully die of thirst.")
        print("Good job!")
    elif do == "something" :
        print("You decide to do something about the endless pit")
        print("Just as you decide that a rabbit appears out of no where and offers his help.")
        print("He says he can help you out of the pit.")
        print("he says you need to pay him first.")

        payment = input("Y/N >")

        if payment == "Y":
            print("The rabbit takes you home and you live your life.")
            print("Good Job!")
        elif payment == "N":
            print("The rabbit leaves you to fall forever. Good job!")

else :
        print("You wake up and realize it was a dream.")
