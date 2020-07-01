# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

class Supermario:

    def __init__(self,name):
        self.name= name

    def jump(self,dest=None):
        print(f"{self.name} is jumping.")
        if dest== "end":
            self.win()
        if dest=="hit":
            self.die()
    
    def run(self,dest=None):
        print(f"{self.name} is running")
        if dest== "end":
            self.win()
        if dest == "hit":
            self.die()

    def win(self):
        print(f"{self.name} meets princess , You win")
        

    def die(self):
        print(f"{self.name} has died , You lose !")

    
s=Supermario("Mario")
s.jump()
s.run("end")