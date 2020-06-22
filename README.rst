Shims: Patching and Mocking Utilities
=====================================

`shims`_ is an Apache2 licensed Python module with patching and mocking
utilities.

The `unittest` package has clever functions for patching modules and
objects. Unfortunately, the common interface is not very readable:

.. code-block:: python

   import unittest
   from unittest.mock import patch

   class TestThing(unittest.TestCase):
       @patch("a.b.c")
       @patch("x.y.z")
       @patch("foo.bar.baz")
       @patch("one.two.three")
       def test_thing(self, mock_three, mock_baz, mock_z, mock_c):
           ...

   if __name__ == "__main__":
       unittest.main()

Now, raise your hand if you've ever confused the order of `patch` decorators
and the order of the arguments (me, times :100:)?

Also, raise your hand if you've struggled to find the right string argument for
`patch` :wave:?

Patch is a great utility but the decorator pattern is not very readable. The
`patch` function actually returns patch objects. And patch objects include
`start()` and `stop()` methods. But these methods are hard to invoke
automatically without decorators using `unittest`.

Furthermore, the patch target is referenced using strings to identify the
object to patch. Most editors lack go-to-definition support for these strings
which sometimes results in even less readable code.

Pytest now to the rescue! Here's the same code, now using Pytest:

.. code-block:: python

   from unittest.mock import MagicMock
   import pytest

   import a.b
   import x.y
   import foo.bar
   import one.two

   def test_thing(monkeypatch):
       mock_c = MagicMock()
       monkeypatch.setattr(a.b, "c", mock_c)
       mock_z = MagicMock()
       monkeypatch.setattr(x.y, "z", mock_z)
       mock_baz = MagicMock()
       monkeypatch.setattr(foo.bar, "baz", mock_baz)
       mock_three = MagicMock()
       monkeypatch.setattr(one.two, "three", mock_three)
       ...

   if __name__ == "__main__":
       pytest.main([__file__])

We're no longer abusing the decorator pattern in Python but it's still not very
reasonable. The fixture idea is a good one and shims goes a bit farther with it.

Here's the same code, now using shims:

.. code-block:: python

   import pytest

   import a.b
   import x.y
   import foo.bar
   import one.two

   def test_thing(shims):
       mock_c = shims.patch(a.b.c)
       mock_z = shims.patch(x.y.z)
       mock_baz = shims.patch(foo.bar.baz)
       mock_three = shims.patch(one.two.three)
       ...

   if __name__ == "__main__":
       pytest.main([__file__])

The problems solved with shims:

0. Decorator pattern replaced with function calls.

0. Targets used directly rather than by strings.

0. MagicMock objects are created automatically.

The end goal is to integrate shims into pytest itself.


Features
--------

- Pure-Python
- Pytest Support (Optional)
- Developed on Python 3.8
- Tested on CPython 3.6, 3.7, 3.8 and PyPy, PyPy3
- Tested using GitHub Actions on Linux, Mac, and Windows

.. image:: https://github.com/grantjenks/python-shims/workflows/integration/badge.svg
   :target: http://www.grantjenks.com/docs/shims/


Quickstart
----------

Installing `shims`_ is simple with `pip <http://www.pip-installer.org/>`_::

  $ pip install shims

You can access documentation in the interpreter with Python's built-in help
function:

.. code-block:: python

   >>> import shims
   >>> help(shims)                         # doctest: +SKIP


Tutorial
--------

The `shims`_ module provides utilities for patching and mocking.

.. code-block:: python

   >>> import urllib.request
   >>> response = urllib.request.urlopen('http://www.example.com/').read()
   >>> print(response[:63].decode())
   <!doctype html>
   <html>
   <head>
       <title>Example Domain</title>


.. code-block:: python

   >>> import shims
   >>> mock_urlopen = shims.patch(urllib.request.urlopen)
   >>> mock_urlopen.return_value = '<test response>'
   >>> urllib.request.urlopen('http://www.example.com/')
   '<test response>'
   >>> shims.stop()


Reference
---------

* `shims Documentation`_
* `shims at PyPI`_
* `shims at GitHub`_
* `shims Issue Tracker`_

.. _`shims Documentation`: http://www.grantjenks.com/docs/shims/
.. _`shims at PyPI`: https://pypi.python.org/pypi/shims/
.. _`shims at GitHub`: https://github.com/grantjenks/python-shims/
.. _`shims Issue Tracker`: https://github.com/grantjenks/python-shims/issues/


License
-------

Copyright 2020 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.

.. _`shims`: http://www.grantjenks.com/docs/shims/
