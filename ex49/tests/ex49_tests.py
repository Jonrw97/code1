from nose.tools import *
from ex49 import parse


def test_sentence():
    s1 = parse.Sentence(('noun', 'john'), ('verb', 'ran'), ('direction', 'left'))
    assert_equal(s1.subject, 'john')
    assert_equal(s1.verb, 'ran')
    assert_equal(s1.obj, 'left')

def test_peek():
    assert_equal(parse.peek([('verb', 'jump')]),('verb'))
    assert_equal(parse.peek([]), None)

def test_match():
    assert_equal(parse.match([('verb', 'run')], 'verb'), ('verb', 'run'))
    assert_equal(parse.match([], 'verb'), None)

def test_skip():
    assert_equal(parse.skip([('stop', 'the'), ('verb', 'run')], 'stop'), None)
    assert_equal(parse.skip([('verb', 'go')], 'stop'), None)
    assert_equal(parse.skip([('stop', 'in')], 'stop'), None)
    assert_equal(parse.skip([], 'stop'), None)

def test_parse_verb():
    assert_equal(parse.parse_verb([('verb', 'jump')]), ('verb', 'jump'))

def test_parse_subject():
    assert_equal(parse.parse_subject([('verb', 'jump')]), ('noun', 'player'))
    assert_equal(parse.parse_subject([('noun', 'jon')]), ('noun', 'jon'))

def test_parse_object():
    assert_equal(parse.parse_object([('noun', 'door')]), ('noun', 'door'))
    assert_equal(parse.parse_object([('direction', 'up')]), ('direction', 'up'))

#def test_raise():
#    assertRaises(ParseError(parse.parse_verb([('noun', 'door')])))
