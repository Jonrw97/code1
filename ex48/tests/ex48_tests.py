from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result,[('direction', 'north'),
                         ('direction', 'south'),
                         ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("GO Kill eaT")
    assert_equal(result, [('verb', 'go'),
                            ('verb', 'kill'),
                            ('verb', 'eat')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                            ('stop', 'in'),
                            ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                            ('noun', 'princess')])

def tests_numbers():
    assert_equal(lexicon.scan("1234"), [('numbers', '1234')])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('numbers', '3'),
                            ('numbers', '91234')])

def test_errors():
    assert_equal(lexicon.scan("asdfasdfasdf"), [('error', 'asdfasdfasdf')])
    result = lexicon.scan("bear ias princess")
    assert_equal(result, [('noun', 'bear'),
                            ('error', 'ias'),
                            ('noun', 'princess')])
