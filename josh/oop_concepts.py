## oop examples

# Create an object and draw a hexagon with the turtle module
# The drawing needs to stay on the screen when done

# from turtle import *

# red_turtle=Turtle()
# red_turtle.color("red")

class Animal():
    def __init__(self, name, pet, sound):
        self.name =name
        self.pet =pet
        self.sound =sound
        
    def speak(self):
        print(self.sound)
    
    def pet_info(self):
        print("My",self.pet,"has the name",self.name,"they make sound",self.sound)
    

dog =Animal("XIRT","IT","HAVHAV")
snake=Animal("SURUNUR","ILAN","FISS")

snake.pet_info()
dog.speak()      
    

        
        