from nose.tools import *
from gothonweb.planisphere import *


def test_room():
    central_corridor = Room("Central Corridor",
                """text CentralCorridor
                """)
    generic_death = Room("Game Over", death[randint(1,5)])
    assert_equal(central_corridor.name, "Central Corridor")
    assert_equal(central_corridor.paths, {})
    assert_true(generic_death== 1 or 2 or 3 or 4 or 5)

def test_room_paths():
    laser_weapon_armory = Room("Laser Weapon Armory",
            """text LaserWeaponArmory
            """)

    the_bridge = Room("The Bridge",
            """text TheBridge
            """)

    escape_pod = Room("Escape Pod",
            """text EscapePod
            """)

    laser_weapon_armory.add_paths({'the_bridge' : the_bridge,
                                    'escape_pod' : escape_pod})
    assert_equal(laser_weapon_armory.go('the_bridge'), the_bridge)
    assert_equal(laser_weapon_armory.go('escape_pod'), escape_pod)

def test_map():
    central_corridor = Room("Central Corridor",
            """text CentralCorridor
            """)

    laser_weapon_armory = Room("Laser Weapon Armory",
            """text LaserWeaponArmory
            """)

    the_bridge = Room("The Bridge",
            """text TheBridge
            """)

    escape_pod = Room("Escape Pod",
            """text EscapePod
            """)
    the_end_winner = Room("The End",
            """text The End Winner
            """)

    the_end_loser = Room("The End",
            """text The End Loser
            """)

    central_corridor.add_paths({'the_bridge':the_bridge,
                                'escape_pod':escape_pod,
                                'laser_weapon_armory':laser_weapon_armory})
    the_bridge.add_paths({'the_end_winner' : the_end_winner})
    escape_pod.add_paths({'the_end_loser' : the_end_loser})
    laser_weapon_armory.add_paths({'run_back':central_corridor})


    assert_equal(central_corridor.go('the_bridge'), the_bridge)
    assert_equal(central_corridor.go('escape_pod').go('the_end_loser'), the_end_loser)
    assert_equal(central_corridor.go('laser_weapon_armory').go('run_back'), central_corridor)

def test_gothon_game_map():
    start_room = load_room(START)
    assert_equal(start_room.go('shoot!'), generic_death)
    assert_equal(start_room.go('dodge!'), generic_death)

    room = start_room.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
