from .core import Shims

_shims = Shims()

patch = _shims.patch
stop = _shims.stop

__title__ = "shims"
__version__ = "0.0.1"
