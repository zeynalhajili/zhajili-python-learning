## oop examples

# Create an object and draw a hexagon with the turtle module
# The drawing needs to stay on the screen when done

# from turtle import *

# red_turtle=Turtle()
# red_turtle.color("red")

# class Animal():
#     def __init__(self, name, pet, sound):
#         self.name =name
#         self.pet =pet
#         self.sound =sound
        
#     def speak(self):
#         print(self.sound)
    
#     def pet_info(self):
#         print("My",self.pet,"has the name",self.name,"they make sound",self.sound)
    

# dog =Animal("XIRT","IT","HAVHAV")
# snake=Animal("SURUNUR","ILAN","FISS")

# snake.pet_info()
# dog.speak()      
   
# class Player():
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#         self.team=None
          
#     def show_stats(self):
#         print("Player name is",self.name)
#         print("Player score for this year is",self.score)
#         print("Team: ",self.team)
        
#     def select_team(self):
#         team_selection =input("Which team he will be playing this year:?\n")
#         self.team=team_selection
 

# player1 =Player("Zeynal","90")
# player2 =Player("John","80")

# player2.select_team()
# player1.select_team()

# player1.show_stats()
# player2.show_stats()


class Rectangle():
    def __init__(self,width,length):
        self.width =width
        self.length =length
    
    def information(self):
        print(f"This is rectangle and it's length is {self.length} and it's width is {self.width}")
    
    def calculate_perimeter(self):
        self.perimeter = 2*(self.width + self.length)
        return self.perimeter

    def calculate_area(self):
        self.area = self.width * self.length
        return self.area
    
    def updated_length(self,length):
        self.updated = (self.length -length) * self.width
        return self.updated

a = int(input("Please enter length:\n"))
b = int(input("Please enter width:\n"))

rect1 = Rectangle(a,b)
rect1.information()
print("Perimeter is: ",rect1.calculate_perimeter())
print("Area is: ",rect1.calculate_area())
