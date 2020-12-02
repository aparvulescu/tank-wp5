material = ['Ti-6Al-4V','Ti-3Al-2.5V','Al 2219-T851']
yieldstrength = [880e6, 500e6, 352e6]

def MatSelec(R,yieldstrength):
    p = 20e5
    t1lst = []
    t2lst = []

    for i in yieldstrength:
        tcyl = (p * R) / i
        tcap = (p * R) / (2 * i)
        t1lst.append(tcyl)
        t2lst.append(tcap)

    return t1lst,t2lst


