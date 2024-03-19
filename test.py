import unittest
from dict2 import Dict2, KeyNotFoundException

class TestDict2(unittest.TestCase):
    def test_store_and_access_values(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        self.assertEqual(obj['a'], 1)
        self.assertEqual(obj['b'], 2)
        self.assertEqual(obj['c'], 3)
    
    def test_custom_exception(self):
        obj = Dict2()
        with self.assertRaises(KeyNotFoundException):
            val = obj['a']
    
    def test_iteration(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        keys = [key for key in obj]
        self.assertEqual(keys, ['a', 'b', 'c'])
    
    def test_missing_key(self):
        obj = Dict2()
        obj['a'] = 1
        with self.assertRaises(KeyNotFoundException):
            val = obj['b']



if __name__ == '__main__':
    unittest.main()
