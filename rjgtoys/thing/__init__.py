"""

.. autoclass:: Thing

"""

import collections.abc


class Thing(dict):
    """
    A :class:`dict`-like thing that behaves like a JavaScript object;
    attribute access and item access are equivalent.  This makes writing
    code that operates on things read from JSON or YAML much simpler
    because there's no need to use lots of square brackets and string
    quotes.

    It also understands about getting items with dots in their names:
    ``something['x.y']`` will return an item called ``x.y`` if one exists,
    but otherwise will try to return ``something['x']['y']``.

    """

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getitem__(self, name):
        """Get an item, allowing dots to separate path components."""

        try:
            return super(Thing, self).__getitem__(name)
        except KeyError:
            if '.' not in name:
                raise
            # Otherwise try harder...

        (prefix, tail) = name.split('.', 1)

        try:
            return self[prefix][tail]
        except (TypeError, KeyError):
            raise KeyError(name)

    def __getattr__(self, name):
        """As __getitem__ but raise AttributeError rather than KeyError"""

        try:
            return self.__getitem__(name)
        except KeyError:
            raise AttributeError(name)

    @classmethod
    def from_object(cls, src=None, **kwargs):
        """Convert `src` to a :class:`~rjgtoys.thing.Thing`, replacing all
        internal mapping objects by instances of :class:`~rjgtoys.thing.Thing` too.

        If `src` is ``None``, treat it as an empty :class:`dict`.

        If there are ``kwargs``, do ``Thing.from_object(kwargs)`` and merge
        the result into the converted ``src``.


        """

        if kwargs:
            if src is not None:
                dst = cls.from_object(src)
            else:
                dst = cls()
            dst.update(cls.from_object(kwargs))
            return dst

        if isinstance(src, cls):
            return src

        if isinstance(src, collections.abc.Mapping):
            return cls((k, cls.from_object(v)) for (k, v) in src.items())

        if isinstance(src, (str, bytes)):
            return src

        if isinstance(src, collections.abc.Iterable):
            return src.__class__(cls.from_object(item) for item in src)

        return src
