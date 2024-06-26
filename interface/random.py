# DO NOT CHANGE THIS FILE
import random

def set_targets(myFleet, enemyFleet):
  '''
  Targeting Stragey that simply select a random target that has not been destroyed yet. Very poor combat capabilities!

  DO NOT CHANGE THIS FUNCTION.
  '''

  # do not shoot at destroyed ships
  valid_ships = []
  for ship in enemyFleet.ships:
    if ship.hull > 0:
      valid_ships.append(ship)

  # shoot at a random target
  for ship in myFleet.ships:
    for weapon in ship.weapons:
      if len(valid_ships) > 0:
        weapon.target = random.choice(valid_ships)
      else:
        # to prevent weapons shooting on anihalated fleets
        weapon.target = None
