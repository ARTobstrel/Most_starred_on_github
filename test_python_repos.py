import unittest

from python_repos import url, get_res


class MyListTest(unittest.TestCase):
    """Testing request on GitHub"""
    def test_get_res(self):
        status_code = get_res(url).status_code
        self.assertEqual(status_code, 200)


if __name__ == '__main__':
    unittest.main()
