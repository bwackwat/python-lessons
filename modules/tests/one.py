import unittest
import os
import sys

print("FILE: " + __file__)
print("DIR: " + os.path.dirname(os.path.abspath(__file__)))
print(sys.path)
print(os.getcwd())

working_dir = os.path.basename(os.path.normpath(os.getcwd()))
print(working_dir)

if working_dir == "python-lessons":
    from ..models import User
else:
    from modules.models import User

class TestOne(unittest.TestCase):

    def test_name(self):
        use_name = "Joe"

        test_user = User(use_name)

        self.assertEqual(test_user.name, use_name)
        self.assertTrue(test_user.name == use_name)

    def test_bad_name(self):
        use_name = ""

        with self.assertRaises(Exception):
            User(use_name)


if __name__ == '__main__':
    unittest.main()
