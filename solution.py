import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
    def __init__(self, ID):
        self.weights = numpy.random.rand(3, 2) * 2 - 1
        self.myID = ID

    def Set_ID(self, ID):
        self.myID = ID

    # old evaluate function used for hill climber algorithm
    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system(f"python3 simulate.py {directOrGUI} {self.myID} &")
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)
        fitnessFile = open(f"fitness{self.myID}.txt", 'r')
        self.fitness = float(fitnessFile.readline())
        fitnessFile.close()

    # runs simulation
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system(f"python3 simulate.py {directOrGUI} {self.myID} &")

    # writes fitness to fitness file after simulation is complete
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)
        fitnessFile = open(f"fitness{self.myID}.txt", 'r')
        self.fitness = float(fitnessFile.readline().strip())
        fitnessFile.close()
        os.system(f"rm fitness{self.myID}.txt")

    # changes one synaptic weight in the robot's neural network
    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    # creates world using pyrosim
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-3, 3, 0.5], size=[1, 1, 1])
        pyrosim.End()

    # creates robot using pyrosim
    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.End()

    # generates brain using pyrosim
    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(0, 3):
            for currentColumn in range(0,2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + 3,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
