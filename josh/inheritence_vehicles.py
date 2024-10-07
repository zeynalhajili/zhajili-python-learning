class Vehicles(): # parent class
    def __init__(self,make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        
    def check_origin(self):
        if self.make.lower() in ["ford", "tesla", "chevy"]: #fixed by chatgpt
        # if self.make.lower() == "ford" or self.make.lower() == "tesla" or self.make.lower() == "chevy" #my solution
            return "American Made"
        else:
            return "Imported"
        
    def model_check(self):
        print(f"This car is {self.model}")
    
    def year_check(self):
        if self.year >= 2000:
            return "Car from 21st century"
        else:
            return "This is old car!"
    
    def check_price(self,max_price):
        if max_price < self.price:
            print(f"Since you can pay {max_price}$, then this car is in your budget!")
        else:
            print("It is over budget")

class Styles(Vehicles): # child class
    def __init__(self,make, model, year, price,number_of_doors):
        super().__init__(make,model,year,price)
        self.number_of_doors = number_of_doors
    
    def get_doors(self):
        if self.get_doors == 4:
            return "This is family car"
        else:
            return "This is sport car"
        
car1 = Vehicles("Ford","Bilmirem",1991,3000) # first object
car2 = Vehicles("Toyota","Corolla",2020,32000) # second object
car3 = Styles("BMW","X3",2021,52000,6) # third object
car4 = Styles("Mercedes","C-Class ",2016,32000,5) # fourth object
car5 = Styles("Lamborgini","Aventedor",2024,132000,2) # fifth object

# print(car1.check_origin())
# print(car1.model_check())
# print(car1.year_check())
print(car4.get_doors())
car4.check_price(60)
car5.check_price(177777)
print(car5.check_origin())
car5.model_check()