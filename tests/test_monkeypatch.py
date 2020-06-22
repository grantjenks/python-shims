"""Tests for Pytest's monkeypatch fixture.

"""

import datetime as dt


def test_setattr(monkeypatch):
    # given
    y2k = dt.date(2000, 1, 1)
    monkeypatch.setattr(dt.date, "today", lambda: y2k)

    # when
    today = dt.date.today()

    # then
    assert today == y2k
