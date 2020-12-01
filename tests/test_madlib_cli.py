from madlib_cli import __version__
from madlib_cli.madlib import*

def test_version():
    assert __version__ == '0.1.0'


def test_read():
    content="""Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."""
    actual =read_File("assets/Game.txt")
    expected = content
    assert actual == expected

def test_raw_Content():
    content = 'Hello {samer} and {bashar}'
    actual =raw_Content(content)
    expected = 'Hello {} and {}'
    assert actual == expected