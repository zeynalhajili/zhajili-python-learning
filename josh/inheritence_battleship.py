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

from time import sleep

class Spaceship(): # parent class
    def __init__(self,name,health,shield):
        self.shield =shield
        self.name = name
        self.health = health
    
    def ship_info(self):
        print(f"Ship name is {self.name}")
        print(f"Ship health is {self.health}")
        print(f"Ship shield is {self.shield}")

class BattleShip(Spaceship):
    def __init__(self, name, health, shield,weapon_type,fleet):
        super().__init__(name, health, shield)
        self.weapon_type = weapon_type
        self.fleet =fleet
        self.destroyed = False
        
    def ship_info(self):
        super().ship_info()
        print(f"Weapon Type: {self.weapon_type}")
        print(f"Fleet: {self.fleet}")
        
        
    def attack(self,bad_guy):
        
        if bad_guy.shield > 0:
            # Reduce shield first, then we will start to reduce health
            bad_guy.shield -= 30
            print(f"{self.name} attacked {bad_guy.name}. Shield reduced to {bad_guy.shield}.")   
        else:
            # If shield is down, reduce health
            bad_guy.health -= 30
            print(f"{self.name} attacked {bad_guy.name}. Health reduced to {bad_guy.health}.")

        # Check if the enemy ship is destroyed
        if bad_guy.health <= 0:
            bad_guy.destroyed = True
            print(f"{bad_guy.name} has been destroyed!")


# Create two instances of BattleShip from different fleets
federation_ship = BattleShip("USS Enterprise", 80, 100, "Laser Cannons", "Federation")
alliance_ship = BattleShip("Alliance Destroyer", 68, 100, "Plasma Guns", "Alliance")

# Print initial ship info
# print("Initial Ship Information:")
# federation_ship.ship_info()
# print("\n")
# alliance_ship.ship_info()

print(f"Battle is starting between {federation_ship.name} and {alliance_ship.name}")

while not federation_ship.destroyed and not alliance_ship.destroyed:
    # federation ship will attack first
    federation_ship.attack(alliance_ship)    
    sleep(2)

    # If the Alliance ship is destroyed, stop the loop
    if alliance_ship.destroyed:
        print(f"{federation_ship.name} won battle!")
        break    
    
    # alliance ship will attack second
    alliance_ship.attack(federation_ship)   
    sleep(2)
    if federation_ship.destroyed:
        print(f"{alliance_ship.name} won battle!")
        break


        