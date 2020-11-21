"""
Demonstrate some awkward cases.

"""

from rjgtoys.thing import Thing


data = Thing.from_object({
    'a.b': 1,
    'c': {
        'd.e': 2
    },
    'f.g': {
        'h': 3
    }
})

assert data['a.b'] == 1

try:
    assert data.a.b == 1
except AttributeError:
    print("You can't 'split' a dotted item name and use it as two attributes")

# The search for a point to 'split' an attribute path is not exhaustive:

# These work:

assert data['c']['d.e'] == 2

assert data['c.d.e'] == 2

try:
    assert data.c.d.e == 2
except:
    print("This is another case of splitting a dotted name")

try:
    assert data['f.g.h'] == 3
except KeyError:
    print("An attribute path is always split 'from the left'")

