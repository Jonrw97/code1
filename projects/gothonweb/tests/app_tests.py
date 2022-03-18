from nose.tools import *
from flask import sessions
from app import app
import sys

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)

    rv = web.get('/', follow_redirects=False)
    assert_equal(rv.status_code, 302)

def test_login():
    rv = web.get('/login', follow_redirects=True)
    assert_equal(rv.status_code, 200)

    data = {'player_name':'test'}
    rv = web.post('/login', follow_redirects=True, data=data)
    assert_in(b'test', rv.data)
    assert_in(b"Central Corridor", rv.data)


    sys.stdout.flush()

def test_game_happy():
    rv = web.get('/game?player_name=test', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Central Corridor", rv.data)

    data = {'action':'tell a joke'}
    rv = web.post('/game?player_name=test', follow_redirects=True, data=data)
    assert_in(b"Laser Weapon Armory", rv.data)

    data = {'action':'0123'}
    rv = web.post('/game?player_name=test', follow_redirects=True, data=data)
    assert_in(b"The Bridge", rv.data)

    data = {'action':'slowly place the bomb'}
    rv = web.post('/game?player_name=test', follow_redirects=True, data=data)
    assert_in(b"Escape Pod", rv.data)
    data = {'action':'2'}
    rv = web.post('/game?player_name=test', follow_redirects=True, data=data)
    assert_in(b"The End", rv.data)

    sys.stdout.flush()

def game_over():
    data = {'action':'shoot!'}
    rv = web.post('/game?player_name=test', follow_redirects=True, data=data)
    assert_in(b"Game Over", rv.data)
