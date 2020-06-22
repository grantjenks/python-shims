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
