from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere
from gothonweb import game_state
app = Flask(__name__)

@app.route("/")
def index():
    #this is used to setup the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("login"))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method =="GET":
        render_template("login.html")
    elif request.method =="POST":
        player_name = request.form.get('player_name')
        player = game_state.get_or_create_player(player_name)
        session.put("player_name", player.name)
        return redirect(url_for("game"))
    else:
        raise error(f"Unhandled Method{request.method}")

@app.route('/game', methods=['POST','GET'])
def game():
    current_player_name=session.get("player_name")
    current_player=game_state.get_or_create_player(player_name)
    room_name = current_player.get(current_game_room)
    if request.method =="GET":
        if room_name:
            room =planisphere.load_room(room_name)
            print(f"in game get {room_name}={room}")
            return render_template("show_room.html", room=room, current_player=current_player)
        else:
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

        if not next_room:
            session['room_name'] = planisphere.name_room(room)
        else:
            session['room_name'] = planisphere.name_room(next_room)
    return redirect(url_for("game"))

app.secret_key ='AX0d9s9cd/?%HalJis '

if __name__ == "__main__":
    app.run(threaded = True)
