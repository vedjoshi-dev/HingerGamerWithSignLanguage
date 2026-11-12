from a1_state import State

class Agent:
    def __init__(self, name="A9"):
        self.name = name
        self.mode = ['minimax', 'alphabeta']
    
    def __str__(self):
        return f"{self.name}, your mode is: {self.mode}"
    


        