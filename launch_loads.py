
import math

# column buckling
# inputs: E, L, R, m

materials = ['Ti-6Al-4V','Ti-3Al-2.5V','Al 2219-T851']
yieldstrength = [880e6, 500e6, 352e6]
youngsm = [113.8e9, 100e9, 73.1e9]
g = 9.81
nu = [0.342, 0.3, 0.33]  # for aluminium poisson's ratio
 

def bucklingCheck(im, L, R, t1, m):
    p = 20e5
    P = 4.3 * g * m
    E = youngsm[im]
    A = 2 * math.pi * R * t1
    I = math.pi * R*R*R * t1
    Q = (p/E) * (R/t1)**2
    lamda = math.sqrt((12/(math.pi**4))*((L*L*L*L)/((R*R)*(t1*t1))*(1-nu[im]**2)))
    k = lamda + (12/math.pi**4) * (L*L*L*L/(R*R * t1*t1)) * (1 - nu[im]*nu[im]) * (1/lamda)  

    # column buckling
    sigma_cr1 = (math.pi**2) * E * I / (A * L*L)
    sigma_tank = P / A
    diff_col = sigma_cr1 - sigma_tank
    
    # shell buckling
    sigma_cr2 = (1.983 - 0.983 * math.exp(-23.14 * Q)) * k * ((math.pi**2 * E) / (12*(1 - nu[im]**2))) * (t1 / L)**2
    diff_shell = sigma_cr2 - sigma_tank

    return (diff_col, diff_shell, sigma_tank, sigma_cr1, sigma_cr2, Q, k, P)
