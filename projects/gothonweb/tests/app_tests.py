from nose.tools import *
from app import app
import sys

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    print("test 1")
    rv = web.get('/', follow_redirects=True)
    print(rv.request.path)
    assert_equal(rv.status_code, 200)

    rv = web.get('/', follow_redirects=False)
    assert_equal(rv.status_code, 302)

    print("test 2")
    rv = web.get('/game', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Central Corridor", rv.data)

    print("test 3")
    data = {'action':'shoot!'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_in(b"Game Over", rv.data)

    sys.stdout.flush()
