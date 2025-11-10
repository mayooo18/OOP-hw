class Procedure:
    def __init__(self, name, date, practitioner, charge ):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    def get_name(self):
        return self.name
    
    def get_date(self):
        return self.date
    
    def get_practitioner(self):
        return self.practitioner
    
    def get_charge(self):
        return self.charge
    
    def set_name(self, name):
        self.name = name                                            

    def set_date(self, date):
        self.date = date
    
    def set_practitioner(self, practitioner):
        self.practitioner = practitioner
    
    def set_charge(self, charge):
        self.charge = charge
    
    def __str__(self):
        return f"Procedure: {self.name}, Date: {self.date}, Practitioner: {self.practitioner}, Charge: ${self.charge:.2f}."