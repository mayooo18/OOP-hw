class Patient:
    def __init__(self, firstname, lastname, address, phone, emergency_contact):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phone = phone
        self.emergency_contact = emergency_contact

    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname
    
    def get_address(self):
        return self.address
    
    def get_phone(self):
        return self.phone
    
    def get_emergency_contact(self):
        return self.emergency_contact
    
    def set_firstname(self, firstname):
        self.firstname = firstname
    
    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone
    
    def set_emergency_contact(self, emergency_contact):
        self.emergency_contact = emergency_contact

    def __str__(self):
        return f"Patient: {self.firstname} {self.lastname}, Address: {self.address}, Phone: {self.phone}, Emergency Contact: {self.emergency_contact}."
    
