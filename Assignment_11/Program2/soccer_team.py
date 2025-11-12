class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def playstyle(self):
        return f"{self.name} plays as a {self.position}."
    
class Goalkeeper(Player):
    def playstyle(self):
        return f"{self.name} is a goalkeeper, specializing in shot-stopping and commanding the defense."
    
class Defender(Player):
    def playstyle(self):
        return f"{self.name} is a defender, focusing on preventing the opposition from scoring."

class Midfielder(Player):
    def playstyle(self):
        return f"{self.name} is a midfielder, orchestrating play and linking defense with attack."

class Forward(Player):
    def playstyle(self):
        return f"{self.name} is a forward, leading the attack and aiming to score goals."

