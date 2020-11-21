"""
Example from the docs.

"""

from rjgtoys.thing import Thing


data = {
 "result" : {
    "status": "success",
    "value": {
       "type": "person",
       "name": "Bob",
       "address": {
          "street": "High Street",
          "town": "Chigley"
        }
     }
   }
}

def print_items(data):

    print(
        "The {type} called {name} lives in {town}".format(
            type=data['result']['value']['type'],
            name=data['result']['value']['name'],
            town=data['result']['value']['address']['town']
        )
    )


def print_attrs(data):
    print(
        "The {type} called {name} lives in {town}".format(
            type=data.result.value.type,
            name=data.result.value.name,
            town=data.result.value.address.town
        )
    )

# The raw data can be printed:

print("Print raw data...")

print_items(data)

try:
    print_attrs(data)
except AttributeError:
    print("The raw data does not support attribute access")

# Convert to a Thing...

print("Now convert...")

data = Thing.from_object(data)

print_items(data)

print_attrs(data)


