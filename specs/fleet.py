from specs.ship import Fighter, Destroyer, Cruiser, Battleship
import random

class Fleet:
  def __init__(self, userid = None):
    '''
    Creates a Fleet by reading in a matching text file in the fleets / folder
    DO NOT CHANGE THIS FUNCTION.
    '''
    if userid:
      self.name = userid
      self.ships = []
      self.read_fleet_file()
    else:
      self.name = "random"
      self.ships = create_random_ships()

  def read_fleet_file(self, target_cost=100):
    '''
    This function attempts to load a fleet file and ensures a fleet file is valid.
    '''
    # TODO Phase 1
    for i in range(100):
      f = Fighter("R")
      self.ships.append(f)


  def get_weapons(self, ship_type):
    '''
    Returns a list of all weapons in the fleet of ships that have not yet been destroyed and belong to the given ship type.
    '''
    # TODO Phase 2
    return []

  def __str__(self):
    """
    Returns a string with the summary of a fleet.
    """
    # TODO Phase 2
    return "F | TODO..."

  def get_stats(self):
    """
    Returns a dictionary with the fleets most important values.
    """
    # TODO: Phase 2
    stats = {
      "cost": 0,
      "ships": 0,
      "hull": 0,
      "armor": 0,
      "shields": 0,
      "total_cost": 0,
      "total_ships": 0,
      "total_hull": 1, # 1 just to avoid an intial div/0 error
      "total_armor": 1,
      "total_shields": 1,
      "damage_taken": 0
    }

    return stats

  def list_ships(self):
    # DO NOT CHANGE THIS METHOD
    print("T |  Hull  | Armor | Shield |  PD  |  E  | DPR |")
    print("==|========|=======|========|======|=====|=====|")
    for ship in self.ships:
      print(ship)

  def regenerate_shields(self):
    """
    When called (at the end of a combat round) will regenerate shields.
    DO NOT MODIFY THIS METHOD.
    """
    for ship in self.ships:
      # try, because this won't work until you have implemented the classes.
      try:
        if ship.hull > 0 and ship.shields > 0 and ship.shields < ship.max_shields:
          ship.shields = min(ship.max_shields, ship.shields + ship.shield_regen)
      except:
        # if one ship fails, all will fail so simply return here (performance)
        return

def create_random_ships(target_cost = 100):
  """
  This function will return a list of randomly generated ships.
  DO NOT CHANGE THIS FUNCTION.
  """
  cost = 0
  ships = []

  while(cost != target_cost):
    # choose a random ship type
    type = random.choice("FFFFDDDCCB")

    # if ship type would exceed command points try again,
    # otherwise increase command points add new ship to list.
    if type == 'B' and cost + 8 > target_cost:
      continue

    elif type == 'B':
      cost += 8
      ships.append(Battleship(random_weapons(4) + random_defenses(3)))

    elif type == 'C' and cost + 4 > target_cost:
      continue

    elif type == 'C':
      cost += 4
      ships.append(Cruiser(random_weapons(3) + random_defenses(2)))

    elif type == 'D' and cost + 2 > target_cost:
      continue

    elif type == 'D':
      cost += 2
      ships.append(Destroyer(random_weapons(2) + random_defenses(1)))

    elif type == 'F':
      cost += 1
      ships.append(Fighter(random_weapons(1)))

  return ships

def random_weapons(count):
  # DO NOT CHANGE THIS FUNCTION
  s = ""
  while len(s) < count:
    s += random.choice("RLT")
  return s

def random_defenses(count):
  # DO NOT CHANGE THIS FUNCTION
  s = ""
  while len(s) < count:
    module = random.choice("SAEP")
    if module == "E" and "E" in s:
      continue
    s += module
  return s
