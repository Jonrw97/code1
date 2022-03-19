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
    'throwbomb': generic_death,
    'placebomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0123': the_bridge,
    '*' : generic_death
})

central_corridor.add_paths({
    'shootgun': generic_death,
    'dodgeguard': generic_death,
    'telljoke': laser_weapon_armory
})

START = central_corridor
START.add_paths({'START':central_corridor})

def get_start_room():
    return START.go('START')

