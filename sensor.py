import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self, linkName: str):
        self.linkName = linkName
        self.values = numpy.zeros(c.SIMULATION_TIME)

    def Get_Value(self, t):
        if self.values[t]:
            self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)


    def Save_Values(self):
        numpy.save(f'data/{self.linkName}SensorValues.npy', self.values)


