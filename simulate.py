import pybullet as p
from time import sleep

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0) # remove side bars
for i in range(1, 1000):
    p.stepSimulation()
    sleep(1/200)
    print(i)

p.disconnect()
