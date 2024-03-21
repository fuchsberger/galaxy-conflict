# from random import random

class Weapon:
  def __init__(self):
    '''
    Base constructor for weapons
    '''
    # TODO Phase 1
    pass

  def fire(self, combat_round):
    '''
    First checks if a weapon is eligible for firing, otherwise do nothing (charge).

    Resolves a weapon applying damage to a specific target.

    If a hit would deduct more damage than the remaining shields the remaining damage of that specific shot is voided. E.g. A ship has 100 shields left. Your weapon made 150 damage. Instead of disabling the shields and doing 50 damage to the armor of the target it will only disable the shield. The next weapon hit will damage armor. Also make sure hull, armor and shields only go down to 0, not become negative values.
    '''
    # TODO Phase 2
    pass

class Railgun(Weapon):
  # TODO Phase 1
  def __init__(self, dmg_modifier):
    pass

class Laser(Weapon):
  # TODO Phase 1
  pass

class Torpedo(Weapon):
  # TODO Phase 1
  pass
