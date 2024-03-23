"""
This File contains some of the actual tests we used in Gradescope.
It gives clues on how we tested your files. You should be able to run this file.
"""

import unittest
from specs.ship import Frigate

class TestDir(unittest.TestCase):
    # Phase 1.1 - Testing Ships and Defense Modules (Test 1.1.1)
    def test_ship_frigate(self):
        """
        Testing the creation of a full Frigate (T).
        """
        ship = Frigate("T")
        self.assertEqual(ship.hull, 100, "Frigate(T) hull should be 100")
        self.assertEqual(ship.max_hull, 100, "Frigate(T) max_hull should be 100")
        self.assertAlmostEqual(ship.evasion, 0.8, 6, "Frigate(T) evasion should be 0.8")
        self.assertAlmostEqual(ship.pd, 0.0, 6, "Frigate(T) pd should be 0.0")
        self.assertEqual(ship.shield_regen, 5, "Frigate(T) shield_regen should be 5")
        self.assertAlmostEqual(ship.max_shields, 50, 6, "Frigate(T) max_shields should be 50")
        self.assertAlmostEqual(ship.shields, 50, 6, "Frigate(T) shields should be 50")
        self.assertAlmostEqual(ship.max_armor, 100, 6, "Frigate(T) max_armor should be 100")
        self.assertAlmostEqual(ship.armor, 100, 6, "Frigate(T) armor should be 50")
        self.assertEqual(ship.cost, 1, "Frigate(T) cost should be 1")


if __name__ == "__main__":
    unittest.main()
