import unittest
from Game import check_win
from Game import check_tie

class MyTestCase(unittest.TestCase):
    def test_1horizontal_win(self):
        board = [
            ["O","O","O"],
            ["X","O","X"],
            ["X","X","O"]]
        player = "O"
        self.assertTrue(check_win(player, board)) # add assertion here

    def test_2horizontal_win(self):
        board = [
            ["X","O","X"],
            ["O","O","O"],
            ["X","X","O"]]
        player = "O"
        self.assertTrue(check_win(player, board)) # add assertion here


    def test_3horizontal_win(self):
        board = [
            ["X","X","X"],
            ["X","O","X"],
            ["O","O","O"]]
        player = "O"
        self.assertTrue(check_win(player, board)) # add assertion here

    def test_left_diagonal_win(self):
        board = [
            ["X","O","O"],
            ["O","X","X"],
            ["O","O","X"]]
        player = "X"
        self.assertTrue(check_win(player, board)) # add assertion here


    def test_right_diagonal_win(self):
        board = [
            ["O","O","X"],
            ["O","X","X"],
            ["X","O","O"]]
        player = "X"
        self.assertTrue(check_win(player, board)) # add assertion here

    def test1_vertical_win(self):
        board = [
            ["X", "O", "X"],
            ["X", "O", "X"],
            ["X", "O", "O"]]
        player = "X"
        self.assertTrue(check_win(player, board))  # add assertion here

    def test2_vertical_win(self):
        board = [
            ["O", "X", "O"],
            ["O", "X", "X"],
            ["X", "X", "O"]]
        player = "X"
        self.assertTrue(check_win(player, board))  # add assertion here

    def test3_vertical_win(self):
        board = [
            ["O", "O", "X"],
            ["O", "O", "X"],
            ["X", "O", "X"]]
        player = "X"
        self.assertTrue(check_win(player, board))  # add assertion here

    def test_full_board_no_tie(self):
        board = [
            ["O"," ","O"],
            ["O","X","X"],
            ["X","X","O"]]
        self.assertFalse(check_tie(board)) # add assertion here

    def test_full_board_with_tie(self):
        board = [
            ["X","O","X"],
            ["X","O","O"],
            ["O","X","O"]]
        self.assertTrue(check_tie(board)) # add assertion here

    def test_full_board_with_many_spaces(self):
        board = [
            [" ","O","O"],
            [" ","O","X"],
            ["X","X","O"]]
        self.assertFalse(check_tie(board)) # add assertion here
if __name__ == '__main__':
    unittest.main()
