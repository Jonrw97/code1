from gothonweb import planisphere
class Player(object):

    def __init__(self, player_name):
        self.player_name = player_name
        self.current_game = "planisphere"
        self.game_count = 0
        self.current_game_room = planisphere.START

    def get_current_game_room(self):
        return self.current_game_room

players = {

}

def get_or_create_player(player_name):
    if player_name in players:
        return players[player_name]

    players[player_name] = Player(player_name)
    return players[player_name]
