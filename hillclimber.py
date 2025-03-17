from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate(directOrGUI='GUI')
        for currentGenerations in range(0, c.NUMBER_OF_GENERATIONS):
            self.Evolve_For_One_Generation()
        self.child.Evaluate(directOrGUI='GUI')

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(directOrGUI='DIRECT')
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(f"parent:{self.parent.fitness} child:{self.child.fitness}")