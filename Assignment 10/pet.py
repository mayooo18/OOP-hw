class Pet:

    def __init__(self, name, animal_type, age ):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def get_name(self):
        return self.name
    
    def get_animal_type(self):
        return self.animal_type
    
    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.animal_type}."
    