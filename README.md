# `Thing`: A Python `dict` that behaves a bit like a JavaScript object

A `Thing` is a subclass of `dict` that behaves a little like
a Javascript object, insofar as 'item' style access - `x['foo']`
- and 'attribute' style access - `x.foo` - are equivalent, and can
be used interchangeably, subject of course to the limitation imposed
by Python syntax itself, that an attribute name in `x.name` has to be
a constant.


Read the documentation at http://rjgtoys.readthedocs.org/projects/thing/
