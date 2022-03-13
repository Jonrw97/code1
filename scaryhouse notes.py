from sys import exit
import random

MESSAGES = {
    'basement_1': {
        'intro':
            """
You slowly regain consciousness and realize you are in a cell.
It is quite dark with just one small window for light.
You notice a picture frame on the wall, also a note on the floor.
            """
    }
}

OUTSIDE = 'outside'
BASEMENT = 'basement'
HALLWAY = 'foyer'
DEAD = 'dead'

VALID_GAME_LOCATIONS = [OUTSIDE, BASEMENT, HALLWAY, DEAD]



def game_over():
    print("GAME OVER")
    exit(0)

def parse_command(cmd, allowed_verbs, allowed_nouns):
    # cmd string split by ' '
    # extract verb
    # extract the noun
    # allowed verbs = ['open', 'knock', 'close', 'hit']
    # allowed nouns = ['door', 'window']
    return True # if extracted verb in allowed_verbs and extracted noun in allowed_nouns

    # return False


# RICHARD
def outside():
# def start():

    game_loop(OUTSIDE)


    print("""There are rumours of an abandoned house that
has hidden treasures inside, while looking for the house
you see a building appear out of nowhere.
Its small and only has 1 window and 1 door.
What will you do? """)


    entry = input("\n> ")
 
    if entry == "enter door" or entry == "door" or entry == "open door":
        print("You open the door and walk inside.")
        print("You are greeted by a butler.")
        print("He asks you to come have some tea in the kitchen.")
        print("As you walk into the kitchen the butler hits you over the head and you lose consciousness.")
        # RICHARD
        # basement()
        return BASEMENT


    elif entry == "open window" or entry ==  "window" or entry == "enter window":
        print("The window is locked, you get hit over the head and lose consciousness.")
        basement()
    elif entry == "knock on door"or entry == "knock":
        print("A butler opens the door but then promptly asks you to leave the property.")
        print("You go home having achieved nothing other than having the manners to knock first.")
        print("GAME OVER")
    elif entry == "knock on window":
        print("You knock on the window and it shatters")
        print("The butler shoots you on sight.")
        print("You died. Normal people knock on doors not windows.")
        print("GAME OVER")
    else:
        print("That's not going to work, you give up and go home.")
        print("GAME OVER")



# RICHARD
def basement(inventory):
    cell_key = False
    # print("You slowly regain consciousness and realize you are in a cell.")
    # print("It is quite dark with just one small window for light.")
    # print("You notice a picture frame on the wall, also a note on the floor.")

    print(MESSAGES['basement_1']['intro'])

    while True:
        print("Now what?")
        cell = input("\n>")

        # RICHARD
        if parse_command(cell, allowed_verbs=['check', 'look'], allowed_nouns=['picture', 'frame']):
            print(MESSAGES['basement_1']['solve_frame_puzzle'])
            inventory['cell_key'] = True
            # cell_key = True
            return HALLWAY, inventory

        elif parse_command(cell, allowed_verbs=['look'], allowed_nouns=['window']):
            # RICHARD
            print(MESSAGES['basement_1']['window_too_short'])



        if  cell == "frame" or cell == "picture" or cell == "check picture" or cell == "check frame" or cell == "picture frame" or cell == "check picture frame" or cell == "look at picture frame" or cell == "look at picture" or cell == "look at frame":
            # RICHARD
            print(MESSAGES['basement_1']['solve_frame_puzzle'])
            cell_key = True

        elif cell == "look out window"or cell == "window" or cell == "check window":
            print("You are too short to see out the window.")

        elif cell == "note" or cell == "read note":
            print("You pickup the note, the note says:")
            print("\nYou have been detained for trespassing on private property.")
            print("You will be released when the master of the house returns.")
            print("He will then decide to press charges or not.")
            print("The butler\n")

        elif cell == "open cell" or cell == "open cell door" or cell == "open door" or cell =="open":
            if cell_key:
                print("You open the cell and head up some stairs.")
                print("You walk into a hallway with 3 doors.")
                print("The first door is to your left, there seems to be some noise coming from this door.")
                print("The second door is straight ahead of you, it looks like the front door.")
                print("The third door is to your right.")
                print("Which door will you take?")
                hallway = input("\n>")

                if hallway == "left" or hallway == "left door" or hallway == "first door" or hallway == "1":
                    print("You enter the door on your left.")
                    print("This is the kitchen, you look around and hear someone behind.")
                    print("You turn around to see the butler.")
                    print("'We Can't have you leaving before the master gets home'the butler says as he knocks you out.")
                    basement2()

                elif hallway == "second door" or hallway == "2" or hallway == "straight door" or hallway == "straight" or hallway == "middle" or hallway =="middle door" :
                    print("You open the second door and find yourself outside.")
                    print("You take a couple steps forward and turn around to go back inside but the house has disappearred")
                    print("You decide to give up and go home.")
                    print("GAME OVER")
                    exit(0)
                elif hallway == "third door" or hallway == "3" or hallway == "right" or hallway == "right door":
                    print("You enter the door on your right.")
                    study()

                else:
                    print("That is not going to work, you hear someone behind you.")
                    print("You turn around to see the butler.")
                    print("'We Can't have you leaving before the master gets home'the butler says as he knocks you out.")
                    basement2()
            else:
                print("The cell is locked.")

        else:
            print("That's not going to work.")




def basement2():
    cell_key = False
    print("You slowly regain consciousness and realize you are back in the cell.")
    print("You notice the picture frame is back on the wall, also the note is still on the floor.")

    while True:
        print("Now what?")
        cell = input("\n>")

        if cell == "frame" or cell == "picture" or cell == "check picture" or cell == "check frame" or cell == "picture frame" or cell == "check picture frame" or cell == "look at picture frame" or cell == "look at picture" or cell == "look at frame":
            print("You walk over to the picture frame and see the words don't let the butler catch you again.")
            print("You flip over the frame and take the key to the cell.")
            cell_key = True

        elif cell == "look out window"or cell == "window" or cell == "check window":
            print("You are too short.")

        elif cell == "note" or cell == "read note":
            print("You pickup the note, the note says:")
            print("\nYou have been detained for trespassing on private property.")
            print("You will be released when the master of the house returns.")
            print("If you persist to be a nuisance drastic measures will be taken.")
            print("The butler\n")

        elif cell == "open cell" or cell == "open cell door" or cell == "open door" or cell =="open":
            if cell_key:
                # RICHARD
                return HALLWAY
                # print("You open the cell and head up some stairs.")
                # print("You walk into a hallway with 3 doors.")
                # print("The first door is to your left, there seems to be some noise coming from this door.")
                # print("The second door is straight ahead of you, it looks like the front door.")
                # print("The third door is to your right.")
                # print("Which door will you take?")
                # hallway = input("\n>")

                if hallway == "left" or hallway == "left door" or hallway == "first door" or hallway == "1" or hallway == "first":
                    print("You enter the door on your left.")
                    print("This is the kitchen, you look around and hear someone behind.")
                    print("You turn around to see the butler.")
                    print("'It seems drastic measures have to be taken.")
                    print("The butler takes drastic measures and you died.")
                    print("Your journey is over.")
                    print("GAME OVER")
                    exit(0)

                elif hallway == "second door" or hallway == "2" or hallway == "second" or hallway == "straight door" or hallway == "straight" or hallway == "middle" or hallway =="middle door":
                    print("You open the second door and find yourself outside.")
                    print("You take a couple steps forward and turn around to go back inside but the house has disappearred")
                    print("You decide to give up and go home.")
                    print("GAME OVER")
                    exit(0)
                elif hallway == "third door" or hallway == "3" or hallway == "first" or hallway == "right" or hallway == "right door":
                    print("You enter the door on your right.")
                    study()

                else:
                    print("That is not going to work, you hear someone behind you.")
                    print("You turn around to see the butler.")
                    print("'It seems drastic measures have to be taken.")
                    print("The butler takes drastic measures and you died.")
                    print("Your journey is over.")
                    print("GAME OVER")
            else:
                print("The cell is locked.")

        else:
            print("That's not going to work.")

# RICHARD
def game_loop(initial_game_location):

    current_game_location = initial_game_location
    inventory = {
        'cell_key': False,
        'knife': False
    }

    while True:
        if current_game_location == OUTSIDE:
            current_game_location, inventory = outside(inventory)
        elif current_game_location == BASEMENT:
            current_game_location, inventory = basement(inventory)
        elif current_game_location == HALLWAY:
            current_game_location = hallway(inventory)
        elif current_game_location == DEAD:
            game_over()






def study():
    hidden_key = False
    black_book = False

    while True:
        print("You are in the study.")
        print("There is a single desk in the middle of the room and a bookshelf against the wall.")
        print("What will you do next?")
        study = input("\n> ")

        if study == "investigate desk" or study == "desk" or study == "check desk":
            if hidden_key:
                print("You have already checked this.")
            else:
                print("You walk over to the desk to check the draws.")
                print("One draw is empty and the other has a key.")
                print("You take the key")
                hidden_key = True

        elif study == "investigate bookshelf" or study == "bookshelf" or study == "check bookshelf":
            if hidden_key:
                if black_book:
                    print("You open the bookshelf and use the master key to open the door.")
                    print("There is a long set of stairs leading down into the darkness.")
                    print("Will you walk down the stairs?")
                    stairs = input("\n>")
                    if stairs == "yes":
                        dark_room()
                    elif stairs == "no":
                        print("You close the hidden door and close the bookshelf.")
                    else:
                        print("You can't do that.")
                elif not black_book:
                    black_book = True
                    print("You walk over to the bookshelf and browse through the books.")
                    print("You notice that there is a black book with no writing on the cover.")
                    print("You pull on the book and realize its a switch, the bookshelf swings open to reveal a door.")
                    print("The door is locked, you use the master key to open it.")
                    print("There is a long set of stairs leading down into the darkness.")
                    print("Will you walk down the stairs?")
                    stairs = input("\n>")
                    if stairs == "yes":
                        dark_room()
                    elif stairs == "no":
                        print("You close the hidden door and close the bookshelf.")
                    else:
                        print("You can't do that.")
                else:
                    print("You can't do that.")


            elif not black_book:
                black_book = True
                print("You walk over to the bookshelf and browse through the books.")
                print("You notice that there is a black book with no writing on the cover.")
                print("You pull on the book and realize its a switch, the bookshelf swings open to reveal a door.")
                print("The door is locked.")
                print("You close the bookshelf to look around the rest of the room.")
            elif black_book:
                print("You open the bookshelf but the door is still locked.")
            else:
                print("Sorry you can't do that.")

        else:
            print("Sorry you can't do that.")




def dark_room():
    chest = False
    print("You walk down the stairs and the door shuts behind you.")
    print("You check the door and it is locked, with no way back you continue to walk down the stairs.")
    print("Eventualy you reach the bottom of the stairs and find yourself in a room.")
    print("In the room is a chest, a sign on the wall and a door.")

    while True:
        dark = input("\n>")

        if dark == "chest" or dark == "open chest":
            print("You walk over to the chest and open it.")
            print("Inside is 10 medkits, a sword and a key.")
            print("You take all the items inside the chest.")
            chest = True
        elif dark == "read sign" or dark == "look at sign" or dark == "sign":
            print("You read the sign on the wall.")
            print("""The sign reads:

There is danger ahead.
Prepare yourself for battle.
Using 'fight' will start a fight.
Using 'attack' will attack the enemy.
Using 'medkit' will heal your wounds. """)

        elif dark == "open door" or dark == "unlock door":
            if chest:
                print("You unlock the door and go into the next room.")
                troll_room()
            else:
                print("The door is locked.")
        else:
            print("That isnt an option.")
            print("There is a chest, a sign on the wall and a door.")


def troll_room():
    print("You enter the next room and see a troll standing infront of the door.")
    print("You walk up to the troll and he says ' You no pass'")
    print("What will you do?")


    health = 100
    damage = 10

    battle = input("\n>")

    if battle == "fight" or battle == "attack":
        print("You attack the troll and he attacks back, keep fighting to win.")
        combat(health, damage)

    elif battle == "talk":
        print("You attempt to talk to the troll but he doesn't care, keep fighting to win.")
        combat(health, damage)

    elif battle == "taunt":
        print("You try to taunt the troll but he hits you. You lose 5 HP.")
        health -= 5
        print("Your HP is now ",health)
        print("Keep fighting to win.")
        combat(health, damage)

    else:
        print("You stumble and fall accidently stabbing yourself.")
        health -= 10
        print("You lose 10 HP, Your HP is now", health)
        print("The troll laughs and swings his club at you but he misses.")
        print("Keep fighting to win.")
        combat(health, damage)


def combat(health, damage):

    troll_health = 100
    troll_damage = 20
    medkit_count = 10

    while True:
        if troll_health <= 0:
            print("\nThe troll is defeated.")
            print("A sword falls from the troll's belt you pick it up and now do increased damage.")
            print("You open the door to the next room and carry on with your journey.\n")
            damage = 20

            treasure_room(health, damage, medkit_count)

        elif health <= 0:
            print("\nThe troll has killed you.")
            print("Your journey ends here.")
            print("GAME OVER")
            exit(0)

        else:
            fight = input("\n>")

            if fight == "attack":
                print("You attack the troll.")

                number = random.randint(0,9)

                if number == 0 or number == 1 or number == 2 or number == 3 or number == 4:
                    print("You hit the troll.")
                    troll_health -= damage
                    print("The troll has", troll_health,"HP left.")
                elif number == 5 or number == 6 or number == 7:
                    print("You hit the troll, it was a critical hit.")
                    troll_health -= damage*2
                    print("The troll has", troll_health,"HP left.")
                else:
                    print("You didnt hit the troll.")
                    print("The troll hit you.")
                    health -= troll_damage
                    print("You have", health,"HP left")
                    print("The troll has", troll_health,"HP left.")
            elif fight == "medkit":
                if medkit_count > 0:
                    print("You use a medkit.")
                    health += 10
                    medkit_count -= 1
                    print("You have", health,"HP left")
                    print("You have", medkit_count,"medkits left.")
                else:
                    print("You have no more medkits.")
            else:
                print("You stab yourself")
                health -= 10
                print("You have", health,"HP left")

def treasure_room(health, damage, medkit_count):

    print("You enter the next room to find it filled with treasure.")
    print("While staring at the treasure someone approaches you.")
    print("'Halt you are trespassing, leave immediately or death will follow.' bellowed The Guardian.")
    print("Seems you are in trouble, now what?")

    while True:
        treasure = input("\n>")

        if treasure == "leave" or treasure == "leave room":
            print("You try to leave the room as The Guardian said but the door is now locked.")
            print("'Is there a problem?' said The Guardian")
            print("Oh I see the door is locked and you can't leave. ")
            print("What a shame seems you have to die then.")
            print("oh no, you are going to die now what?")

            what = input("\n>")
            if what == "attack" or what == "fight":
                print("You attack The Guardian, the fight for your life is on.")
                combat2(health, damage, medkit_count)

            elif what == "talk" or what == "talk to The Guardian" or what == "talk to the guardian" or what == "talk to guardian" or what == "talk to Guardian":
                print("'Oh you wish to talk.")
                talk(health, damage, medkit_count)

            else:
                print("'You stand there and do nothing, what a rude human.'said The Guardian")
                health -= 25
                print("The Guardian attacks you, you take damage.")
                print("You have ", health,"HP left.")
                print("The fight for your life is on.")
                combat2(health, damage, medkit_count)


        elif treasure == "talk" or treasure == "talk to The Guardian" or treasure == "talk to the guardian" or treasure == "talk to guardian" or treasure == "talk to Guardian":
            print("'Oh you wish to talk.' said The Guardian")
            talk(health, damage, medkit_count)

        elif treasure == "attack" or treasure == "fight":
            print("You attack The Guardian, the fight for your life is on.")
            combat2(health, damage, medkit_count)

        else:
            print("'You stand there and do nothing, what a rude human.'said The Guardian")
            health -= 25
            print("The Guardian attacks you, you take damage.")
            print("You have ", health,"HP left.")
            print("The fight for your life is on.")
            combat2(health, damage, medkit_count)


def talk(health, damage, medkit_count):
    print("'Hmmm you are a strange human.'")
    print("'Alright then if you can answer my riddle i will let you leave with whatever you would like.'")
    print("""'You measure my life in hours and I serve you by expiring.
I’m quick when I’m thin and slow when I’m fat.
The wind is my enemy. '""")
    answer = input("\n>")
    if answer == "candle" or answer == "a candle":
        print("'Correct, well done human.'")
        print("You may take as much treasure as you wish and are free to leave, the exit is just behind me.")
        end()

    else:
        print("'That is incorrect, you fail human.'")
        print("'Now you will die'said The Guardian.")
        print("The fight for your life is on.")
        combat2(health, damage, medkit_count)

def combat2(health, damage, medkit_count):
    guardian_hp = 200
    guardian_damage = 30

    while True:
        if guardian_hp <= 0:
            print("\nThe Guardian is defeated.")
            print("You are free to take all the treasure you want.")
            print("With the guardian defeated a door appears and opens.\n")
            end()
        elif health <= 0:
            print("\nThe Guardian has killed you.")
            print("Your journey ends here.")
            print("GAME OVER")
            exit(0)

        else:
            fight = input("\n>")

            if fight == "attack" or fight == "fight":
                print("You attack The Guardian.")

                number = random.randint(0,9)

                if number == 0 or number == 1 or number == 2 or number == 3 or number == 4:
                    print("You hit The Guardian.")
                    guardian_hp -= damage
                    print("The Guardian has", guardian_hp,"HP left.")
                elif number == 5 or number == 6 or number == 7:
                    print("You hit The Guardian, it was a critical hit.")
                    guardian_hp -= damage*2
                    print("The Guardian has", guardian_hp,"HP left.")
                else:
                    print("You didnt hit The Guardian.")
                    print("The Guardian hit you.")
                    health -= guardian_damage
                    print("You have", health,"HP left")
                    print("The Guardian has", guardian_hp,"HP left.")
            elif fight == "medkit":
                if medkit_count > 0:
                    print("You use a medkit.")
                    health += 10
                    medkit_count -= 1
                    print("You have", health,"HP left")
                    print("You have", medkit_count,"medkits left.")
                else:
                    print("You have no more medkits.")
            else:
                print("You stab yourself")
                health -= 10
                print("You have", health,"HP left")

def end():
    print("""You collect up as much treasure as you can before heading towards the door.
There are stairs leading up towards the surface, you make your way up the stairs.
After a long walk up the stairs you eventually reach a door, you try open the door but feel it is stuck.
You push hard against the door, you manage to open the door and are finally out in the open air again.
You notice the house you entered, the front door opens a shadowy figure appears in the doorway.
You see the butler standing in the doorway waving to you as the house slowly disappears.

The house completly disappears, you head home having had one crazy adventure that no one will believe.

YOU WIN
""")
    exit(0)



start()
