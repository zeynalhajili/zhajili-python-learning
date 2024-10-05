class Animal(): # Parent class
    def __init__(self, name, pet, sound):
        self.name =name
        self.pet =pet
        self.sound =sound
        
    def speak(self):
        print(self.sound)
    
    def pet_info(self):
        print("My",self.pet,"has the name",self.name,"they make sound",self.sound)
    
class Fish(Animal): # child class
    
    def swim(self):
        if self.sound == None:
            print("You are a fish")
        else:
            print("You must not be fish...")
            
    def ocean(self):
        self.region = input("From which ocean you are from:\n")
        print(f"{self.name} is from {self.region} ocean")

pet1 = Fish("Nemo","Fish",None)
pet1.pet_info()
pet1.swim()
pet1.ocean()
        
    

 