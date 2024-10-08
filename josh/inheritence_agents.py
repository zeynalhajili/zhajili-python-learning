# Creating classes for our Agents, James Bond and Ethan Hunt
# Create a superclass that takes a name, health and car +
# Create a superclass method that prints off the Agents information +

# Create a child class called Spy, this inherits everything from the parent class
# Add three additional properties of agency, location and killed (killed is set to False) (Ethan hunt will be the bad guy)+


# Create a method to attack/assassinate the other agent, this takes one parameter (an object)
# if the enemys' health is greater than 0, subtract 20 from their health. Print off who has lost 20 health and print off their updated health level
# if the enemys' health is less than or equal to 0, the killed property becomes True, print off " [enemy_name] is dead...."

# Create two instances of the Spy class, one for James Bond, One for Ethan Hunt
# call the method to print off the agents information, then wait 5 seconds
# while ethan_hunts health is greater than 0, both objects call the assassinate method to attack
# After every attack the program should wait 2 seconds before the next

from time import sleep

class Agents(): # parent class
    def __init__(self, name, health, car):
        self.name = name
        self.health = health
        self.car = car
        
    def agent_info(self):
        print(f"Agent name is {self.name}")
        print(f"Agent health is {self.health}")
        print(f"Agent car is {self.car}")
               
class Spy(Agents): # child class, which inherits from Agents Super Class.
    def __init__(self, name, health, car, agency, location):
        super().__init__(name, health, car) # Inheriting from Parent Agents class
        self.agency = agency
        self.location = location
        self.killed = False # We don't need to pass killed as an argument because it's always going to start as False.
    
    def attack(self, enemy):
        if enemy.health > 0:  # Check if the enemy is still alive
            enemy.health -= 20  # Reduce the enemy's health by 20
            print(f"{enemy.name} has lost 20 health. They now have {enemy.health} health.")
            
            if enemy.health <= 0:  # Check if the enemy's health has dropped to 0 or below
                enemy.killed = True  # Mark the enemy as killed
                print(f"{enemy.name} is dead!")  # Print death message
                
    def is_alive(self): # check if agent is live or dead
        return not self.killed
            
james_bond = Spy("James Bond", 81, "Toyota","LR","Istanbul") # create james object
ethan_hunt = Spy("Ethan Hunt", 92,"BMW","VR","London") # create ethan object

while james_bond.is_alive() and ethan_hunt.is_alive():
    james_bond.attack(ethan_hunt)
    sleep(2)
    
    if not james_bond.is_alive():
        break   
    ethan_hunt.attack(james_bond)
    sleep(3)
    
    
print("Gamer Over!")
    






      
        
       
        
        
        





# ethan_hunt.agents_name()
# james_bond.agents_name()