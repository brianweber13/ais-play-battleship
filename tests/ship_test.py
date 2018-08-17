#!/usr/bin/env python3
""" tests ship class """

import unittest

import context
import ais_play_battleship.ship

class ShipTestCase(unittest.TestCase):
    """ standard unittest class. See
    https://docs.python.org/3/library/unittest.html """
    def setUp(self):
        self.test_ship = ais_play_battleship.ship.Ship({
            'name': 'carrier',
            'occupied_squares': set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]),
            })

    def test_hit(self):
        """ tests check_for_hits on a successful hit

         - does method return true on successful hit?
         - does it modify ship's unhit_squares?
         - does it preserve the ship's occupied_squares?
        """
        self.assertTrue(self.test_ship.check_for_hits((3, 0)))
        self.assertEqual(self.test_ship.unhit_squares,
                         set([(0, 0), (1, 0), (2, 0), (4, 0)]))
        self.assertEqual(self.test_ship.occupied_squares,
                         set([(0, 0), (1, 0), (3, 0), (2, 0), (4, 0)]))

    def test_miss(self):
        """ tests check_for_hits on a miss

         - does method return false on a miss?
         - does it leave the ships unhit_squares and occupied_squares
           unmodified?
        """
        self.assertFalse(self.test_ship.check_for_hits((6, 0)))
        self.assertEqual(self.test_ship.unhit_squares,
                         set([(0, 0), (1, 0), (3, 0), (2, 0), (4, 0)]))
        self.assertEqual(self.test_ship.occupied_squares,
                         set([(0, 0), (1, 0), (3, 0), (2, 0), (4, 0)]))

    def test_if_sunk_when_not_sunk(self):
        """ tests both the ship.sunk attribute as well as the
        ship.check_if_sunk() method """
        self.assertFalse(self.test_ship.sunk)
        self.assertFalse(self.test_ship.check_if_sunk())

    def test_if_sunk_when_actually_sunk(self):
        """ sinks the ship, then tests if it's sunk

         - is sunk attribute false?
         - does check_if_sunk return false?
         - are occupied_squares preserved?
         - is unhit_squares now the empty set?
        """
        self.test_ship.check_for_hits((0, 0))
        self.test_ship.check_for_hits((1, 0))
        self.test_ship.check_for_hits((2, 0))
        self.test_ship.check_for_hits((3, 0))
        self.test_ship.check_for_hits((4, 0))
        self.assertEqual(self.test_ship.unhit_squares,
                         set([]))
        self.assertEqual(self.test_ship.occupied_squares,
                         set([(0, 0), (1, 0), (3, 0), (2, 0), (4, 0)]))
        self.assertTrue(self.test_ship.sunk)
        self.assertTrue(self.test_ship.check_if_sunk())

if __name__ == '__main__':
    unittest.main()
