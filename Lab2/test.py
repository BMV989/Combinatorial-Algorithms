from main import bfs
import unittest


class TestBFS(unittest.TestCase):

    def test_1(self):
        n = 4
        ad_matrix = [
            [0, 1, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(bfs(n, ad_matrix), None)

    def test_2(self):
        n = 3
        ad_matrix = [
            [0, 1, 1],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(bfs(n, ad_matrix), None)

    def test_3(self):
        n = 5
        ad_matrix = [
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(bfs(n, ad_matrix), None)

    def test_4(self):
        n = 4
        ad_matrix = [
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [0, 0, 1, 0]
        ]
        self.assertEqual(bfs(n, ad_matrix), [1, 2, 3])

    def test_5(self):

        n = 4
        ad_matrix = [
            [0, 1, 0, 0],
            [1, 0, 1, 1],
            [0, 1, 0, 1],
            [0, 1, 1, 0]
        ]
        self.assertEqual(bfs(n, ad_matrix), [2, 3, 4])

    def test_6(self):
        n = 5
        ad_matrix = [
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0]
        ]
        self.assertEqual(bfs(n, ad_matrix), [3, 4, 5])


if __name__ == '__main__':
    unittest.main()
