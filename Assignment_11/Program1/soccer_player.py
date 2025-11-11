class Player:
    def __init__(self, name):
        self.name = name

    def play_style(self):
        return " Plays Soccer" 
    
class Forward(Player):
    def play_style(self):
        return f"{self.name} makes smart runs, finds space, and finishes chances."
    
class Midfielder(Player):
    def play_style(self):
        return f"{self.name} controls the tempo, distributes passes, and supports both defense and attack."
    
class Defender(Player):
    def play_style(self):
        return f"{self.name} marks opponents, intercepts passes, and clears the ball from danger."
    
class Goalkeeper(Player):
    def play_style(self):
        return f"{self.name} saves shots, commands the defense, and distributes the ball effectively."