
import math

# column buckling
# inputs: E, L, R, m

yieldstrength = [880e6, 500e6, 352e6]
g = 9.81
nu = 0.334  # for aluminium poisson's ratio
 

def bucklingCheck(im, L, R, t1, m):
    p = 20e5
    P = 4.3 * g * m
    E = yieldstrength[im]
    A = 2 * math.pi * R * t1
    I = math.pi * R**3 * t1
    Q = (p/E) * (R/t1)**2
    k = lamda + (12/math.pi**4) * (L**4/(R**2 * t1**2)) * (1 - nu**2) * (1/lamda)  

    # column buckling
    sigma_cr1 = (math.pi**2) * E * I / (A * L**2)
    sigma_tank = P / A
    diff_col = sigma_cr1 - sigma_tank
    
    # shell buckling
    sigma_cr2 = (1.983 - 0.983 * math.exp(-23.14 * Q)) * k * ((math.pi**2 * E) / 12*(1 - nu**2)) * (t1 / L)**2
    diff_shell = sigma_cr2 - sigma_tank

    return (diff_col, diff_shell)
