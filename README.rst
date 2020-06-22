Pytest Shims: Patching and Mocking Utilities
============================================

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
automatically without decorators using `unittest`. Furthermore, the interface
uses strings to identify the objects to pass. Most editors lack
go-to-definition support for these strings which sometimes results in even less
readable code.

`Pytest`_ now to the rescue! Here's the same code, now using Pytest:

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




// monkeypatch works well in pytest but doesn't go far enough. End goal is to
integrate pytest-shims into pytest itself.


Features
--------

- Pure-Python
- Pytest Support (Optional)
- Developed on Python 3.8
- Tested on CPython 3.6, 3.7, 3.8 and PyPy, PyPy3
- Tested using GitHub Actions on Linux, Mac, and Windows

.. image:: https://github.com/grantjenks/pytest-shims/workflows/integration/badge.svg
   :target: http://www.grantjenks.com/docs/pytest-shims/


Quickstart
----------

Installing `ivenv`_ is simple with `pip <http://www.pip-installer.org/>`_::

  $ pip install ivenv

You can access documentation in the interpreter with Python's built-in help
function:

.. code-block:: python

   >>> import ivenv
   >>> help(ivenv)
   >>> help(ivenv.activate)
   >>> help(ivenv.deactivate)


Tutorial
--------

The `ivenv`_ module provides two functions for managing virtual environments:

.. code-block:: python

   >>> from ivenv import activate, deactivate

The `activate` function accepts a path to a virtual environment directory and
"activates" that virtual environment within the Python shell.

.. code-block:: python

   >>> activate('path/to/venv/directory')

The `deactivate` function takes no arguments and "deactivates" the virtual
environment within the Python shell.

.. code-block:: python

   >>> deactivate()

It's also possible to use `ivenv`_ from IPython or Jupyter notebooks. To begin,
load the `ivenv` extension:

.. code-block:: shell

   %load_ext ivenv

Once the extension is loaded, the "magic" commands: `%activate` and
`%deactivate` may be used just as their corresponding functions.

.. code-block:: shell

   %activate path/to/venv/directory
   %deactivate


Reference
---------

* `ivenv Documentation`_
* `ivenv at PyPI`_
* `ivenv at GitHub`_
* `ivenv Issue Tracker`_

.. _`ivenv Documentation`: http://www.grantjenks.com/docs/ivenv/
.. _`ivenv at PyPI`: https://pypi.python.org/pypi/ivenv/
.. _`ivenv at GitHub`: https://github.com/grantjenks/python-ivenv/
.. _`ivenv Issue Tracker`: https://github.com/grantjenks/python-ivenv/issues/


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

.. _`ivenv`: http://www.grantjenks.com/docs/ivenv/
