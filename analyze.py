import matplotlib
matplotlib.use('TkAgg')  # Or 'Agg', 'Qt5Agg', etc., depending on your system
import matplotlib.pyplot as plt
import numpy as np


backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
targetAngles_BackLeg = np.load('data/targetAngles_BackLeg.npy')
targetAngles_FrontLeg = np.load('data/targetAngles_Front_Leg.npy')
# plt.plot(backLegSensorValues, label="Back Leg Sensor", linewidth=3)
# plt.plot(frontLegSensorValues, label="Front Leg Sensor")
plt.plot(targetAngles_BackLeg, label="Target Angles Back Leg")
plt.plot(targetAngles_FrontLeg, label="Target Angles Front Leg")
plt.legend()
plt.show()
