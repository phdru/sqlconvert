
import unittest

__all__ = ['TestCase', 'main']


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


def main():
    try:
        unittest.main(testRunner=unittest.TextTestRunner())
    except SystemExit as msg:
        result = msg.args[0]
    else:
        result = 0
    raise SystemExit(result)
