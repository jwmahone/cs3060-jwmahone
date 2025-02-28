import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.sensors: dict[str, SENSOR] = {}
        self.motors: dict[str, MOTOR] = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)



    def Act(self, desiredAngle):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode('utf-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)



    def Think(self):
        self.nn.Update()
        self.nn.Print()

