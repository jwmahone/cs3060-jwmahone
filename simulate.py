import pybullet as p
import pybullet_data
from time import sleep
import pyrosim.pyrosim as pyrosim
import numpy
import random

SIMULATION_TIME = 1000

amplitude_BackLeg = numpy.pi / 2
frequency_BackLeg = 16
phaseOffset_BackLeg = 0

amplitude_FrontLeg = numpy.pi / 2
frequency_FrontLeg = 16
phaseOffset_FrontLeg = 8

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(SIMULATION_TIME)
frontLegSensorValues = numpy.zeros(SIMULATION_TIME)
targetAngles_BackLeg = amplitude_BackLeg * numpy.sin(frequency_BackLeg * numpy.linspace(0, 2 * numpy.pi, SIMULATION_TIME) + phaseOffset_BackLeg)
targetAngles_FrontLeg = amplitude_FrontLeg * numpy.sin(frequency_FrontLeg * numpy.linspace(0, 2 * numpy.pi, SIMULATION_TIME) + phaseOffset_FrontLeg)

for i in range(0, SIMULATION_TIME):
    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_BackLeg[i],
        maxForce=30)
    sleep(1/2400)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_FrontLeg[i],
        maxForce=30
    )

p.disconnect()

numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
numpy.save('data/targetAngles_BackLeg.npy', targetAngles_BackLeg)
numpy.save('data/targetAngles_Front_Leg.npy', targetAngles_FrontLeg)
