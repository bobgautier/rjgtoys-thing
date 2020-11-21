The Details
===========

Instead of :class:`dict`, use :class:`rjgtoys.thing.Thing`.

It has a constructor that works exactly like :class:`dict`,
so it can be a drop-in replacement::

   from rjgtoys.thing import Thing

   x = Thing(a=1, b=2)

   y = Thing((('a',1), ('b',2)))

If you access an item that doesn't exist, you get :exc:`KeyError` and if you
access an attribute that doesn't exist, you get :exc:`AttributeError`.

Converting :class:`dict` to :class:`~rjgtoys.thing.Thing`
=========================================================

When you construct a :class:`~rjgtoys.thing.Thing` from a :class:`dict`,
all may not be well::

   data = {
      'a': 1,
      'b': {
         'c': {
            'd': 3
          }
       }
    }

   data_thing = Thing(data)

The resulting ``data_thing`` will indeed be a :class:`~rjgtoys.thing.Thing` but
the constructor does not do a 'deep copy' or even a 'deep conversion', and so
the internal :class:`dict` elements will remain as :class:`dict`.

That will defeat any attempt to use attribute access past the first level::

   part_b = data_thing.b   # This is fine

   d_value = data_thing.b.c.d  # This will fail; data_thing.b is a dict

The solution is to use :meth:`~rjgtoys.thing.Thing.from_object`.  That does
a 'deep copy' and will convert any internal :class:`dict` objects
into :class:`~rjgtoys.thing.Thing` ::

  data_thing = Thing.from_object(data)

.. automethod:: rjgtoys.thing.Thing.from_object


Other Awkward Cases and Caveats
===============================


Items don't hide existing attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Items that have the same name as an existing attribute of :class:`dict` are
not available via attribute access: ``items`` is one example; even for
:class:`~rjgtoys.thing.Thing` it is still the method that returns the sequence
of key-value pairs.   So if you build this::

   data = Thing(
      items=[1,2,3]
    )

You will still have to access the data as ``data['items']``, whilst
``data.items()`` will return you the sequence ``(('items', [1,2,3]))``.

Dots in item names are not usable with attribute access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your :class:`~rjgtoys.thing.Thing` has items with names containing dots,
you can always access them using item-style access ``data['a.b.c']`` but
attribute style access is not possible.

Item names with dots cannot always be concatenated with others
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For simple-named item names, you can use 'paths' to navigate
through nested objects::

   data = {
      'a': 1,
      'b': {
         'c': {
            'd': 3
          }
       }
    }

   data_thing = Thing.from_object(data)

   data_thing.b.c.d == 3    # This works
   data_thing['b.c.d']      # So does this

But this fails when the item names themselves contain dots::


   data = {
      'a': 1,
      'b.c': {
            'd': 3
          }
       }
    }

   data_thing = Thing.from_object(data)

   data_thing.b.c.d == 3    # FAILS
   data_thing['b.c.d']      # FAILS

   data_thing['b.c']['d']   # Works (but it would work with a dict too)
