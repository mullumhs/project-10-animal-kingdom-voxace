"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a base class for an animal and derived classes for specific 
               types of animals in an animal kingdom program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Animal that represents a generic animal in an animal kingdom.
# This class should have an initializer with at least three attributes. E.g. name, age, and habitat.
# Add at least two methods for common animal behaviors. E.g. eat and sleep.

class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}, Habitat: {self.habitat}"

# Create at least two derived classes from the Animal class. E.g. Bird and Fish.
# Give each of the derived classes at least one specific behavior. E.g. fly and swim.

class Bird(Animal):
    def __init__(self, name, age, habitat, wing_span):
        super().__init__(name, age, habitat)
        self.wing_span = wing_span

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wing_span} meters.")
    
    def __str__(self):
        return f"{super().__str__()}, Wing Span: {self.wing_span}"

class Fish(Animal):
    def __init__(self, name, age, habitat, fin_length):
        super().__init__(name, age, habitat)
        self.fin_length = fin_length

    def swim(self):
        print(f"{self.name} is swimming with fins of {self.fin_length} cm long.")
    
    def __str__(self):
        return f"{super().__str__()}, Fin Length: {self.fin_length}"

# Additional class that inherits from Bird
class Eagle(Bird):
    def __init__(self, name, age, habitat, wing_span, beak_length):
        super().__init__(name, age, habitat, wing_span)
        self.beak_length = beak_length

    def hunt(self):
        print(f"{self.name} is hunting with a beak length of {self.beak_length} cm.")
    
    def __str__(self):
        return f"{super().__str__()}, Beak Length: {self.beak_length}"

# Create at least two instances of the Animal derived classes with different data.

parrot = Bird(name="Parrot", age=2, habitat="Tropical Forest", wing_span=0.25)
shark = Fish(name="Shark", age=5, habitat="Ocean", fin_length=50)
eagle = Eagle(name="Eagle", age=4, habitat="Mountains", wing_span=2.3, beak_length=7)

# Write code that prints out the details of each animal and calls their specific behaviors.

print(parrot)
parrot.eat()
parrot.sleep()
parrot.fly()

print(f"\n{shark}")
shark.eat()
shark.sleep()
shark.swim()

print(f"\n{eagle}")
eagle.eat()
eagle.sleep()
eagle.fly()
eagle.hunt()
