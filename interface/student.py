import random

def set_targets(myFleet, enemyFleet):
  '''
  This should ensure that each weapon of the attacker's ships
  points towards a valid target (ship) of the defender.
  This function must only change weapons's target property!
  The target property must be a ship in the enemy Fleet.
  '''
  # TODO Phase 3

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
        # to prevent weapons shoot on anihalated fleets
        weapon.target = None
