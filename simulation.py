from world import WORLD
from robot import ROBOT
from time import sleep
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        p.setGravity(0, 0, -9.8)

        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        for i in range(0, c.SIMULATION_TIME):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            sleep(1/1000)

    def __del__(self):

        p.disconnect()


