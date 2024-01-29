import unittest
import os.path


class YourTestCase(unittest.TestCase):

    @unittest.skipIf(not os.path.exists('models/engine/db_storage.py'), "exit")
    def test_something(self):
        # Your test logic here
        pass
