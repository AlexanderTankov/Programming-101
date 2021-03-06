import unittest

from reduce_file_path import reduce_file_path


class Reduce_file_path_test(unittest.TestCase):

    def test_reduce_file_path(self):
        self.assertEqual("/", reduce_file_path("/"))
        self.assertEqual("/", reduce_file_path("/srv/../"))
        self.assertEqual("/srv/www/htdocs/wtf", reduce_file_path("/srv/www/htdocs/wtf/"))
        self.assertEqual("/srv/www/htdocs/wtf", reduce_file_path("/srv/www/htdocs/wtf"))
        self.assertEqual("/srv", reduce_file_path("/srv/./././././"))
        self.assertEqual("/etc/wtf", reduce_file_path("/etc//wtf/"))
        self.assertEqual("/", reduce_file_path("/etc/../etc/../etc/../"))
        self.assertEqual("/", reduce_file_path("//////////////"))
        self.assertEqual("/", reduce_file_path("/../"))
if __name__ == '__main__':
    unittest.main()
