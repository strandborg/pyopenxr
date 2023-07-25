import unittest

import xr


class TestBool(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_atom_methods(self):
        with xr.Instance() as instance:
            self.assertTrue(instance)
            pass  # context manager methods exist
        self.assertFalse(xr.Instance(None))  # None arg yields uninitialized Instance


if __name__ == '__main__':
    unittest.main()
