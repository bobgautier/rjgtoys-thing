import pytest

from rjgtoys.thing import Thing


def test_thing():

    t = Thing(a=1, b=2)

    assert t.a == 1
    assert t.b == 2

    assert t['a'] == 1
    assert t['b'] == 2


def test_thing_path():

    t = Thing(a=1, b=2)
    tt = Thing(t=t, c=3)

    assert tt.t.a == 1
    assert tt.t.b == 2
    assert tt.c == 3

    assert tt['t.a'] == 1
    assert tt['t.b'] == 2
    assert tt['c'] == 3


def test_thing_raises_keyerror():

    t = Thing(a=1, b=2)

    with pytest.raises(KeyError):
        x = t['c']

    with pytest.raises(KeyError):
        y = t['a.b']


def test_thing_raises_attributeerror():

    t = Thing(a=1, b=2)

    with pytest.raises(AttributeError):
        x = t.c

    with pytest.raises(AttributeError):
        y = t.a.b


def test_thing_from_obj():

    f = Thing.from_object

    assert f(1) == 1

    assert f((1,2)) == (1,2)

    assert f([1,2]) == [1,2]

    assert f(dict(a=1, b=2)) == Thing(a=1, b=2)

    assert f(dict(sub=dict(a=1, b=2), c=3)) == Thing(
        sub=Thing(a=1, b=2),
        c=3
    )

def test_thing_from_obj_noop():

    t = Thing(x=1, y=2)

    x = Thing.from_object(t)

    assert x is t

def test_thing_from_obj_kwargs():

    t = Thing(x=1, y=2)

    x = Thing.from_object(t, x=3, z='abc')

    assert x == {
        'x': 3,
        'y': 2,
        'z': 'abc'
    }

def test_thing_from_obj_kwargs_only():

    t = None

    x = Thing.from_object(t, x=3, z='abc')

    assert x == {
        'x': 3,
        'z': 'abc'
    }
