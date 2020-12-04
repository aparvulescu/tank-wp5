import math

Fx = 1427.40
Fy = 899.8 #FY + F1
Fz = 665.70
g = 9.81
F_tot = math.sqrt(Fx**2 + Fy**2 + Fz**2)
m_wp4 = 0.0233


def massAttachments(m, n): # m = mass of tank, n = number of attachments, m_wp4 = mass of lug attachment
    P = 4.3 * g * m
    P_n = P / n
    ratio = F_tot / P_n
    m_att = ratio * m_wp4
    m_atttot = m_att * n
    
    return m_atttot