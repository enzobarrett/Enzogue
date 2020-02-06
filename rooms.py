import random
from hallway import Hallway

class Room:
    def __init__(self):
        self.w = random.randrange(4, 24, 2)
        self.h = random.randrange(4, 24, 2)
        self.genHalls()

    def genHalls(self):
        self.halls = []

        for x in range(random.randrange(1,4)):
            self.halls.append(Hallway())
            
        
    


        

