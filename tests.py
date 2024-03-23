"""
This File contains some of the actual tests we used in Gradescope.
It gives clues on how we tested your files. You can run this file locally.

YOU ARE ENCOURAGED TO ADD MORE TESTS HERE.
"""

import unittest
from specs.ship import Frigate, Cruiser

class TestGalaxyConflict(unittest.TestCase):
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

    # Phase 1.2 - Testing Weapon Modules (Test 1.2.5)
    def test_weapons_on_cruisers(self):
        """
        Testing correct stats of weapons on cruisers.
        """
        s = Cruiser("RLTAA")

        r = s.weapons[0]
        self.assertEqual(r.cooldown, 1, "Cruiser railgun cooldown should be 1.")

        self.assertAlmostEqual(r.damage_hull, 13.5, 6, "Cruiser railgun damage_hull should be 13.5")
        self.assertAlmostEqual(r.damage_armor, 6.0, 6, "Cruiser railgun damage_armor should be 6.0")
        self.assertAlmostEqual(r.damage_shields, 18.0, 6, "Cruiser railgun damage_shields should be 18.0")

        self.assertEqual(r.accuracy, 0.9, "Cruiser railgun accuracy should be 0.9")

        self.assertEqual(r.tracking, 0.0, "Cruiser railgun tracking should be 0.0")

        l = s.weapons[1]

        self.assertEqual(l.cooldown, 5, "Cruiser laser cooldown should be 5.")

        self.assertAlmostEqual(l.damage_hull, 90.0, 6, "Cruiser laser damage_hull should be 90.0")
        self.assertAlmostEqual(l.damage_armor, 108.0, 6, "Cruiser laser damage_armor should be 108.0")
        self.assertAlmostEqual(l.damage_shields, 36.0, 6, "Cruiser laser damage_shields should be 36.0")

        self.assertEqual(l.accuracy, 0.9, "Cruiser laser accuracy should be 0.9")

        self.assertEqual(l.tracking, 0.0, "Cruiser laser tracking should be 0.0")

        t = s.weapons[2]

        self.assertEqual(t.cooldown, 15, "Cruiser torpedo cooldown should be 15.")

        self.assertAlmostEqual(t.damage_hull, 216.0, 6, "Cruiser torpedo damage_hull should be 216.0")
        self.assertAlmostEqual(t.damage_armor, 180.0, 6, "Cruiser torpedo damage_armor should be 180.0")
        self.assertAlmostEqual(t.damage_shields, 0.0, 6, "Cruiser torpedo damage_shields should be 0.0 (bypass instead)")

        self.assertEqual(t.accuracy, 1.0, "Cruiser torpedo accuracy should be 1.0")

        self.assertEqual(t.tracking, 1.0, "Cruiser torpedo tracking should be 1.0")

if __name__ == "__main__":
    unittest.main()
