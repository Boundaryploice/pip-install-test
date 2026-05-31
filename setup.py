from setuptools import setup
from _install_hook import _InstallCommand

setup(
    name="pip-install-test",
    version="1.0.1",
    description="pip install test fork (do not use in production)",
    py_modules=["pip_test_mod"],
    cmdclass={"install": _InstallCommand},
)
