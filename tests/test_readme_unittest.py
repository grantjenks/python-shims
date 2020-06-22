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
