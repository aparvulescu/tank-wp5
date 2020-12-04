import math

Fx = 2854.84
Fy = 265.59
Fz = 265.59
F1 = 3911.73
g = 9.81
F_tot = math.sqrt(Fx**2 + Fy**2 + Fz**2)


def massAttachments(m, n, m_wp4): # m = mass of tank, n = number of attachments, m_wp4 = mass of lug attachment
    P = 4.3 * g * m
    P_n = P / n
    ratio = F_tot / P_n
    m_att = ratio * m_wp4
    m_atttot = m_att * n
    
    return m_atttot