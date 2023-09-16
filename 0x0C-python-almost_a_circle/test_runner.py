import os
import sys
import unittest

# Add the project directory to the Python path
project_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_directory)

if __name__ == '__main__':
    # Discover and run tests in the tests directory
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover('tests')
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
