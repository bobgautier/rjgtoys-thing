See Also
========

This package is not a new idea, and this implementation is simply
my attempt.

Here are some links to others:

A StackOverflow question from someone looking for
a
:class:`~rjgtoys.thing.Thing`-like object:
`<https://stackoverflow.com/questions/2640806/javascript-like-object-in-python-standard-library>`_

The replies mention two examples:

One from from ActiveState: `The simple but handy "collector of a bunch of named stuff"`_

.. _The simple but handy "collector of a bunch of named stuff": https://code.activestate.com/recipes/52308-the-simple-but-handy-collector-of-a-bunch-of-named/



Another, available on PyPi as bunch_ is more substantial and in many ways more
complete than this package.

.. _bunch: https://pypi.org/project/bunch/1.0.0/



One should not forget that :class:`~rjgtoys.thing.Thing` is really just
a quick hack for when you have a structured bit of data that you need to
dive into, and don't feel it's worth writing any better definition of
the structure of that data.   When you *do* have time for that, then I'd
recommend a package like Pydantic_, which can provide you with the tools
to type-check and validate the structure.


.. _Pydantic: https://pydantic-docs.helpmanual.io/


