from launch_loads import bucklingCheck
from materialselection import MatSelec
from mass_calculators import massTankAndProp
from mass_attachments import massAttachments
import numpy as np
import math

print("Hello project WP5!")

materials = ['Ti-6Al-4V','Ti-3Al-2.5V','Al 2219-T851']
yieldstrength = [880e6, 500e6, 352e6]
density = [4430, 4480, 2840]
youngsm = [113.8e9, 100e9, 73.1e9]
mProp = [38.5/2, 187.5/2]
V = [0.12/2, 0.15/2]
fo = 2
ok = 0
n = 4  # number of attachemnts per tank

while fo != 0 and fo != 1:
    fo = int(input("Do you want to calculate dimensions for fuel (0) or oxizidizer (1)?: "))
    if fo != 0 and fo != 1:
        print("Your input is wrong! Only accepted values are 0 (fuel) or 1 (oxidizer). Try again.")
    
maxR = (3 * V[fo] / 4 / math.pi)**(1/3)

for R in np.arange(0.01, maxR, 1e-3):
    L = 1 / (math.pi * R * R) * (V[fo] - 4/3*math.pi*R*R*R)
    if (L > 1.0 or L < 0):
        continue
    at1, at2 = MatSelec(R, yieldstrength)

    MLst = []
    t1lst = []
    t2lst = []
    for i in range(len(materials)):
        t1 = at1[i]
        t2 = at2[i]
        totMass = massTankAndProp(i, L, R, t1, t2, fo)
        diff_col, diff_shell = bucklingCheck(i, L, R, t1, totMass)
        while (diff_col < 0 or diff_shell < 0) and t1 < 0.5e-2:
            t1 += 1e-5
            totMass = massTankAndProp(i, L, R, t1, t2, fo)
            diff_col, diff_shell = bucklingCheck(i, L, R, t1, totMass)
        MLst.append(totMass)
        t1lst.append(t1)
        t2lst.append(t2)

    lowestMass = min(MLst)
    im = MLst.index(min(MLst))
    t1 = t1lst[im]
    t2 = t2lst[im]
    material = materials[im]

    if diff_col > 0 and diff_shell > 0 and L > 0:
        #print(f"Option passes with material = {material}, L = {L:.5f}, R = {R:.5f}, t1 = {t1:.5f}, t2 = {t2:.5f}, mass = {lowestMass:.5f}")
        ok = 1
        
        oldMass = lowestMass
        matt = massAttachments(oldMass, n)
        newMass = oldMass + matt
        while newMass - oldMass >= 0.001:
            oldmatt = matt
            oldMass = newMass
            matt = massAttachments(oldMass, n)
            newMass = oldMass - oldmatt + matt
        # to add buckling check
        # including the attachents
        diff_col, diff_shell = bucklingCheck(i, L, R, t1, newMass) 
        if diff_col > 0 and diff_shell > 0:
            print(f"Option passes with material = {material}, L = {L:.5f}, R = {R:.5f}, t1 = {t1:.5f}, t2 = {t2:.5f}, mass = {newMass:.5f}, mass_hingeless = {lowestMass:.5f}")
            
    else:
        #print(f"diff_col = {diff_col}, diff_shell = {diff_shell}")
        continue

if ok == 0:
    print("No suitable value found.")

