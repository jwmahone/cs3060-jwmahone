import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
import constants as c


class MOTOR:
    def __init__(self, jointName: str):
        self.jointName = jointName
        self.Prepare_Motor_Values(c.AMPLITUDE, c.FREQUENCY, c.PHASE_OFFSET)

    def Prepare_Motor_Values(self, amplitude, frequency, phaseOffset):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phaseOffset = phaseOffset
        self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 2 * numpy.pi,
                                                                                      c.SIMULATION_TIME) + self.phaseOffset)


    def Set_Value(self, t, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=30)

    def Save_Value(self):
        numpy.save(f'data/targetAngles_{self.jointName}', self.motorValues)
