from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):

    """Setup the py.test test runner."""
    
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))
