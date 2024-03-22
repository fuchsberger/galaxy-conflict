import random

# you may import further standard library modules but do not import additional files that you created. The autograder won't be able to load them!

# Add additionally needed ADTS here such as a Priority Queues, Arrays,...

def set_targets(myFleet, enemyFleet):
  '''
  YOUR TOP-SECRET WINNING STRATEGY FOR GALACTIC DOMINANCE.
  '''
  # TODO Phase 3
  # Currently a copy of the random strategy but this should improve.

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
