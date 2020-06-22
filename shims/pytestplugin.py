import pytest

from .core import Shims


@pytest.fixture
def shims():
    shims = Shims()
    yield shims
    shims.stop()
