import matplotlib
matplotlib.use('TkAgg')  # Or 'Agg', 'Qt5Agg', etc., depending on your system
import matplotlib.pyplot as plt
import numpy as np


backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
plt.plot(backLegSensorValues, label="Back Leg Sensor", linewidth=3)
plt.plot(frontLegSensorValues, label="Front Leg Sensor")
plt.legend()
plt.show()
