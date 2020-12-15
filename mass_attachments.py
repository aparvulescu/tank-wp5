import math




def massAttachments(m, n): # m = mass of tank, n = number of attachments, m_wp4 = mass of lug attachment
    Fx = 1427.40
    Fy = 899.8 #FY + F1
    Fz = 665.70
    m_sc = 1477.5
    g = 9.81
    F_tot = math.sqrt(Fx**2 + Fy**2 + Fz**2)
    m_wp4 = 0.0233
    
    P = 4.3 * g * (m + m_sc)
    P_n = P / n
    ratio = P_n / F_tot
    m_att = ratio * m_wp4
    m_atttot = m_att * n
    
    return m_atttot