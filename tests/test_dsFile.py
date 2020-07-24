import unittest
from testfixtures import tempdir, compare
from dsFile import dsFile

class test_dsFile(unittest.TestCase):
    def setUp(self):
        self.func = dsFile("")
 
    def test_1(self):
        self.assertTrue(True)

    # def test_2(self):
    #     self.assertGreaterEqual(int(Config.GetConfigValue("API", "PORT")), 1)

    # def tearDown(self):
    #     print("GONE")
 
if __name__ == '__main__':
    unittest.main()