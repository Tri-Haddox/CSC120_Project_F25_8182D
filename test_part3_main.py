import unittest
from unittest.mock import patch
import main as escaping_game

class TestEscapingGame(unittest.TestCase):

    def setUp(self):
        escaping_game.player = {
            "x": 0,
            "y": 0,
            "name": "Tester",
            "health": 100,
            "coin": 0
        }

    # ------------------ move() ------------------
    def test_move_up_blocked(self):
        escaping_game.move("w")
        self.assertEqual(escaping_game.player["x"], 0)
        self.assertEqual(escaping_game.player["y"], 0)

    def test_move_down(self):
        escaping_game.move("s")
        self.assertEqual(escaping_game.player["x"], 1)

    def test_move_left_blocked(self):
        escaping_game.move("a")
        self.assertEqual(escaping_game.player["y"], 0)

    def test_move_right(self):
        escaping_game.move("d")
        self.assertEqual(escaping_game.player["y"], 1)


    # ------------------ draw_ui() ------------------
    @patch('builtins.print')
    def test_draw_ui_runs(self, mock_print):
        escaping_game.draw_ui(0, 0) 
        self.assertTrue(mock_print.called)


if __name__ == "__main__":
    unittest.main()
    