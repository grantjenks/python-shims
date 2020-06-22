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
    pytest.main()
