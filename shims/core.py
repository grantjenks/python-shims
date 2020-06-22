from unittest.mock import MagicMock, patch

class Shims:
    def __init__(self):
        self._patches = []

    def patch(self, target):
        magic_mock = MagicMock()
        target_path = f'{target.__module__}.{target.__qualname__}'
        patched = patch(target_path, magic_mock)
        patched.start()
        self._patches.append(patched)
        return magic_mock

    def stop(self):
        for patched in self._patches:
            patched.stop()
        self._patches.clear()
