from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
from setuptools import setup, find_packages

setup(
    name='Proyecto',
    version='1.0',
    packages=find_packages(include=['app', 'app.*']),  # Incluir solo el paquete 'app' y sus subpaquetes
)

class RunTestsCommand(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args.split())
        sys.exit(errno)

setup(
    tests_require=['pytest'],
    cmdclass={'test': RunTestsCommand}
)
