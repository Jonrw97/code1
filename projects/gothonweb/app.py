from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere
from gothonweb import game_state
from gothonweb import parse
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method =="GET":
        return render_template("login.html")
    elif request.method =="POST":
        player_name = request.form.get('player_name')
        player = game_state.get_or_create_player(player_name)
        return redirect(url_for("game", player_name = player_name))
    else:
        raise Exception(f"Unhandled Method{request.method}")

@app.route('/play_again')
def play_again():
    player_name = request.args.get('player_name', None)
    player = game_state.get_or_create_player(player_name)
    player.reset_current_game()
    return redirect(url_for("game", player_name = player_name))

@app.route('/game', methods=['POST','GET'])
def game():
    player_name = request.args.get('player_name', None)

    player = game_state.get_or_create_player(player_name)
    room = player.get_current_game_room()
    if request.method =="GET":
        if room:
            return render_template("show_room.html", room=room, player=player, player_name = player_name)
        else:
            raise Exception("No room found")
    else:
        action = request.form.get('action')
        print(action,">>>>>>action")
        parsed_action = parse.parse_sentence(action)
        print(parsed_action,">>>>>>parsed_action")

        if room and parsed_action:
            next_room = room.go(parsed_action)

        if next_room:
            player.save_current_room(next_room)
        else:
            raise Exception("No next room found")
    return redirect(url_for("game", player_name = player_name))

app.secret_key ='AX0d9s9cd/?%HalJis '

if __name__ == "__main__":
    app.run(threaded = True)
