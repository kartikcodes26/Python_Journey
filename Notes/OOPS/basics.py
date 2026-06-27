class Vehicle:
    def __init__(self, name: str, range: int) -> None:
        wheels = 4 # Shared by all objects
        self.range = range
        self.name = name
        self.is_started = False
        
    def start(self) -> None:
        if self.is_started:
            print("The vechicle is already running")
        else:
            self.is_started = True
            print("The vehicle sucessfully started")
        
    def turn_off(self) -> None:
        if self.is_started == False:
            print("The car is already turned off")
            
        else:
            self.is_started = False
            print("Sucessfully turned off the car")
            
    # Dunder methods
    def __add__(self, other):
        print(f"Total range : {self.range + other.range}")
        
    def __mul__(self, other):
        ...
         
    def __str__(self) -> str:
        return f"Name : {self.name} \nRange : {self.range}"
    
    def __repr__(self) -> str:
        ...
        
        
    
car = vehicle("car", 120)
print(car.name)
print(car.range)
car.start()
car.start()
car.turn_off()
car.turn_off()
truck = vehicle("Truck", 80)
print(truck + car)
print(car)

  
