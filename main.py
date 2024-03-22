# run via shell, for example:
# python main.py student random 1

# run directly (with the defaults above):
# python main.py

from os import path
from sys import argv
import importlib.util

from specs.fleet import Fleet, create_random_fleet
from simulation import Simulation

def show_usage() -> None:
    """
    This function displays the program usage and its options.
    DO NOT MODIFY THIS FUNCTION.
    """
    print("Usage: python main.py [left_fleet] [right_fleet] [gui]\n")
    print("[left_fleet] a fleet file, default: student")
    print("[right_fleet] A fleet file, default: mixed)")
    print("[gui] 0 or 1 whether to use GUI or not, default: 1\n")
    print("If fleet files cannot be found will generate and use random fleets.")
    print("If matching target system is not found will use random targeting.\n")


def main() -> None:
    """
    Project 3 Main Program

    This is the main program of Project 3. It has the following usages:

        python main.py [left_fleet] [right_fleet] [0-1]

    When it takes no command line arguments, it sets up student vs mixed without gui.
    If a fleet file cannot be found program will create and use a random fleet.
    If a target system file cannot be found program will use random targeting.

    First option choices:

        student
        frigates
        destroyers
        cruisers
        battleships
        mixed
        random

    Second option choices:

        student
        frigates
        destroyers
        cruisers
        battleships
        mixed
        random

    Note that it is possible to battle against yourself (for example: student vs student).

    DO NOT CHANGE THIS FUNCTION
    """
    args = argv[1:]

    # Set default options
    left_fleet = "student"
    right_fleet = "mixed"
    gui = 1

    # Read left_fleet if it is provided
    if len(args) > 0: left_fleet = args[0]

    # Read right_fleet if it is provided
    if len(args) > 1: right_fleet = args[1]

    # Read gui if it is provided
    if len(args) > 2:
        try:
            gui = int(args[2])
        except:
            print("Cannot parse gui option to an integer\n")
            show_usage()
            exit(-2)
        if gui < 0 or gui > 1:
            print("Incorrect gui option. It should be 0-1\n")
            show_usage()
            exit(-3)

    # Try importing the provided target system, otherwise load random.
    try:
        file_path = f'path/to/{left_fleet}.py'
        spec = importlib.util.spec_from_file_location(left_fleet, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        interface_left = getattr(module, 'set_targets')
    except:
        from interface.random import set_targets as interface_left

    try:
        file_path = f'path/to/{right_fleet}.py'
        spec = importlib.util.spec_from_file_location(right_fleet, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        interface_right = getattr(module, 'set_targets')
    except:
        from interface.random import set_targets as interface_right

    # load fleets
    if path.exists(f"fleets/{left_fleet}.txt"):
        left_fleet = Fleet(left_fleet)
    else:
        left_fleet = Fleet(None)

    if path.exists(f"fleets/{right_fleet}.txt"):
        right_fleet = Fleet(right_fleet)
    else:
        right_fleet = Fleet(None)

    # Run Simulation
    Simulation(left_fleet, right_fleet, interface_left, interface_right, gui)

# avoid running main() in case main.py is imported.
if __name__ == "__main__":
    main()
