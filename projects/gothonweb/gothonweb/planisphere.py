from random import randint
from gothonweb import user_interface
class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
                        user_interface.UI['central_corridor'])

laser_weapon_armory = Room("Laser Weapon Armory",
                            user_interface.UI['laser_weapon_armory'])

the_bridge = Room("The Bridge",
                    user_interface.UI['the_bridge'])

escape_pod = Room("Escape Pod",
                    user_interface.UI['escape_pod'])
the_end_winner = Room("The End",
                        user_interface.UI['the_end_winner'])

the_end_loser = Room("The End",
                        user_interface.UI['the_end_loser'])

death = {
    1 : "You died.  You kinda suck at this.",
    2 : "Your Mom would be proud...if she were smarter.",
    3 : "Such a luser.",
    4 : "I have a small puppy that's better at this.",
    5 : "You're worse than your Dad's jokes."
}

generic_death = Room("Game Over", death[randint(1,5)])

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0123': the_bridge,
    '*' : generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

def get_start_room():
    return load_room(START)

def load_room(name):
    """
    There is a potential secruity problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible secruity problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key
