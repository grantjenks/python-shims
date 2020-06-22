"""Package Setup for pytest-shims

"""

from setuptools import setup
from setuptools.command.test import test as TestCommand

import shims


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox

        errno = tox.cmdline(self.test_args)
        exit(errno)


with open("README.rst") as reader:
    readme = reader.read()

setup(
    name=shims.__title__,
    version=shims.__version__,
    description="Patching and mocking utilities",
    long_description=readme,
    author="Grant Jenks",
    author_email="contact@grantjenks.com",
    url="http://www.grantjenks.com/docs/pytest-shims/",
    license="Apache 2.0",
    packages=["shims"],
    tests_require=["tox"],
    cmdclass={"test": Tox},
    install_requires=["pytest"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    entry_points={"pytest11": ["pytest-shims = shims.pytestplugin"]},
)
