import unittest
from unittest.mock import patch
from io import StringIO
import random
from game import *


class TestGame(unittest.TestCase):

    # --------------- Player Tests ----------------
    def test_player_initialization(self):
        p = player()
        self.assertEqual(p.name, "Tester")
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)
        self.assertEqual(p.health, 100)
        self.assertEqual(p.coin, 0)

    def test_player_movement(self):
        p = player()
        map_size = 5

        p.move("s", map_size)
        self.assertEqual(p.x, 1)

        p.move("d", map_size)
        self.assertEqual(p.y, 1)

        p.move("w", map_size)
        self.assertEqual(p.x, 0)

        p.move("a", map_size)
        self.assertEqual(p.y, 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_player_invalid_move(self, mock_stdout):
        p = player()
        p.move("w", 5)  # moving up at top edge
        self.assertIn("You cannot move that way!", mock_stdout.getvalue())

    # ---------------- GameMap Tests ----------------
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_map_draw(self, mock_stdout):
        p = player()
        gm = GameMap()
        gm.draw(p)

        output = mock_stdout.getvalue()
        self.assertIn("C", output)      # Character
        self.assertIn("M", output)      # Goal tile
        self.assertIn("Health:", output)
        self.assertIn("Coin:", output)

    # ---------------- Game Event Tests ----------------
    def test_check_event_coin(self):
        game = Game()
        game.events = ["find a coin"]
        game.check_event()
        self.assertEqual(game.player.coin, 1)

    def test_check_event_monster(self):
        game = Game()
        game.events = ["meet a monster"]
        game.check_event()
        self.assertEqual(game.player.health, 90)

    def test_check_event_do_nothing(self):
        game = Game()
        game.events = ["do nothing"]
        prev_health = game.player.health
        prev_coin = game.player.coin
        game.check_event()

        self.assertEqual(game.player.health, prev_health)
        self.assertEqual(game.player.coin, prev_coin)

    # ---------------- Game Victory Test ----------------
    @patch('builtins.input', side_effect=(["d"] * 8) + (["s"] * 8))
    @patch('sys.stdout', new_callable=StringIO)
    def test_reach_exit(self, mock_stdout, mock_input):
        game = Game()

        # simulate moves until reaching (8,8)
        game.play()

        self.assertIn("Congratulations! You reach the gate for next level.", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()