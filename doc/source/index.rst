rjgtoys.thing: A Python dict that behaves a bit like a JavaScript object
========================================================================

This package implements a little trick that I find handy to keep code
tidy when I'm dealing with complicated nested dictionary structures,
such as can be returned from REST APIs.

It implements a subclass of :class:`dict` that behaves a little like
a Javascript object, insofar as 'item' style access - ``x['foo']``
- and 'attribute' style access - ``x.foo`` - are equivalent, and can
be used interchangeably, subject of course to the limitation imposed
by Python syntax itself, that an attribute name in ``x.name`` has to be
a constant.

So if you have an object like this, perhaps the result of doing an API call::

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

The instead of having to write this::

  print("The {type} called {name} lives in {town}".format(
        type=data['result']['value']['type'],
        name=data['result']['value']['name'],
        town=data['result']['value']['address']['town']
  ))

You can write this::

  print("The {type} called {name} lives in {town}".format(
        type=data.result.value.type,
        name=data.result.value.name,
        town=data.result.value.address.town
  ))

.. toctree::
   :maxdepth: 2

   detail
   seealso
   getting
   todo




