# from random import random

class Weapon:
  def __init__(self):
    '''
    Base constructor for weapons
    '''
    # TODO Phase 1

    # do not remove the following line, it is needed for phase 2
    # and will contain the current ship this weapon is firing upon:
    self.target = None

  def fire(self, combat_round):
    '''
    Handles applying damage according to the fire rules outlined in the doc.
    '''
    # TODO Phase 2
    pass

class Railgun(Weapon):
  # TODO Phase 1
  def __init__(self, ship):
    pass

class Laser(Weapon):
  # TODO Phase 1
  def __init__(self, ship):
    pass

class Torpedo(Weapon):
  # TODO Phase 1
  def __init__(self, ship):
    pass
