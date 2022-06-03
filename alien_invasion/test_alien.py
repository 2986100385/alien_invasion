from alien import Alien
from alien_invasion import AlienInvasion
import unittest
import time


class TestAlien(unittest.TestCase):
    def test_track_alien(self):
        game = AlienInvasion()
        alien = Alien(game)
        alien.update()
        alien.check_edges()
        game._update_screen()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
