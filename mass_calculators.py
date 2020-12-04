import math
density = [4430, 4480, 2840]

def massTankAndProp(im, L, R, t1, t2, fo):

    if fo == 0:  # fuel
        mProp = 38.5/2 # [kg]
    elif fo == 1:  # oxidixer
        mProp = 187.5/2 # [kg]

    mTank = (L * 2 * R * math.pi * t1 + 4 * math.pi * R * R * t2) * density[im]

    return mTank + mProp
