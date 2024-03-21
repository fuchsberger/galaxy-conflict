from specs.ships import Fighter #, Destroyer, Cruiser, Battleship
import random

class Fleet:
  def __init__(self, userid):
    '''
    Creates a Fleet by reading in a matching text file in the fleets/ folder
    DO NOT CHANGE THIS FUNCTION.
    '''
    self.name = userid
    self.ships = []
    self.read_fleet_file()

  def read_fleet_file(self):
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
    print("T |  H   |  A   |  S   |  PD  |  E   | DPS |")
    print("==|======|======|======|======|======|=====|")
    for ship in self.ships:
      print(ship)

def create_random_fleet():
  """
  This function will update `random.txt` with a new, randomly composed fleet.
  DO NOT CHANGE THIS FUNCTION
  """
  file = open("fleets/random.txt", "w")
  s = ""

  cp = 0
  while(cp != 100):
    # create random ship type
    type = random.choice("FFFFDDDCCB")

    # if ship type would exceed command points try again,
    # otherwise increase command points and fill ship with modules
    if type == 'B' and cp + 8 > 100:
      continue
    elif type == 'B':
      cp += 8
      s += "B " + random_weapon_modules(4) + random_defense_modules(3) + "\n"
    elif type == 'C' and cp + 4 > 100:
      continue
    elif type == 'C':
      cp += 4
      s += "C " + random_weapon_modules(3) + random_defense_modules(2) + "\n"
    elif type == 'D' and cp + 2 > 100:
      continue
    elif type == 'D':
      cp += 2
      s += "D " + random_weapon_modules(2) + random_defense_modules(1) + "\n"
    elif type == 'F':
      cp += 1
      s += "F " + random_weapon_modules(1) + "\n"

  file.write(s)
  file.close()


def random_weapon_modules(count):
  # DO NOT CHANGE THIS FUNCTION
  s = ""
  while len(s) < count:
    s += random.choice("RLT")
  return s

def random_defense_modules(count):
  # DO NOT CHANGE THIS FUNCTION
  s = ""
  while len(s) < count:
    module = random.choice("SAEP")
    if module == "E" and "E" in s:
      continue
    s += module
  return s
