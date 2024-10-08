# Task: Space Battle Simulation
# You will create a simple simulation of a space battle between two ships.

# Requirements:
# Create a parent class called Spaceship:

# It should have the following attributes:
# name (the name of the spaceship),
# health (the health of the spaceship),
# shield (the shield level of the spaceship).
# Create a method ship_info() that prints the spaceship's name, health, and shield.
# Create a child class called BattleShip that inherits from Spaceship:

# Add the following additional attributes:
# weapon_type (the type of weapon the ship uses),
# fleet (the fleet or faction the ship belongs to).
# destroyed (this is initially set to False).
# Override the ship_info() method to also print the weapon_type and fleet of the ship.
# Create a method called attack in the BattleShip class:

# The method should take one parameter (an object) called enemy.
# If the enemy ship's shield is greater than 0, reduce the shield by 30. Print which ship attacked, the enemy ship's name, and its updated shield level.
# If the enemy ship’s shield is less than or equal to 0, reduce the enemy's health by 30. Print which ship attacked, the enemy ship's name, and its updated health level.
# If the enemy ship’s health is less than or equal to 0, mark the enemy ship as destroyed = True and print that the enemy ship has been destroyed.
# Create two instances of the BattleShip class:

# One ship will be from the Federation fleet, and another ship will be from the Alliance fleet.
# Run a battle simulation where the two ships alternate attacking each other until one is destroyed:

# After each attack, print both ships' information.
# Use a loop to continue attacking until one ship’s health drops to 0 or below.

