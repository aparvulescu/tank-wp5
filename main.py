from launch_loads import bucklingCheck
from materialselection import MatSelec
import numpy as np
import math

print("Hello project WP5!")

material = ['Ti-6Al-4V','Ti-3Al-2.5V','Al 2219-T851']
yieldstrength = [880e6, 500e6, 352e6]
density = [4430,4480,2840]

for R in np.arange(0, 1, 1e3):
    L = 1 / (math * R * R) * (V - 4/3*math.pi*R*R*R)

    at1, at2 = MatSelec(R, yieldstrength)

    diff_col, diff_shell = bucklingCheck(im, L, R, t1, m)
