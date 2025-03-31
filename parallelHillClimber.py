from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0

        for i in range(0, c.POPULATION_SIZE):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGenerations in range(0, c.NUMBER_OF_GENERATIONS):
            self.Evolve_For_One_Generation()
        self.Evaluate(self.children)
        #self.Show_Best()

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation(directOrGUI='DIRECT')
        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()



    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print("------------------------------------------------------")
        for key in self.parents:
            print(f"parent:{self.parents[key].fitness} child:{self.children[key].fitness}")

    def Show_Best(self):
        most_fit_solution = self.parents[0]
        for key in self.parents:
            if self.parents[key].fitness < most_fit_solution.fitness:
                most_fit_solution = self.parents[key]
        most_fit_solution.Start_Simulation("GUI")
