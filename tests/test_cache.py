# test_cache.py

import unittest

from src.cache import Cache

class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache(size=4096, associativity=2, block_size=32)

    def test_get_tag_and_set_index(self):
        # Define test cases: (address, expected_tag, index, offset)
        test_cases = [
            (0x7fe89981, 0xffd13, 0xc, 0x1),
            (0x7fe89981, 0xffd13, 0xc, 0x1),
        ]

        for address, expected_tag, expected_index, expected_offset in test_cases:
            tag, index, offset = self.cache.get_tag_index_offset(address)
            self.assertEqual(tag, expected_tag)
            self.assertEqual(index, expected_index)
            self.assertEqual(offset, expected_offset)

if __name__ == '__main__':
    unittest.main()
