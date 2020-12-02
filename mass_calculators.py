import math

def massTank&Fuel(im, L, R, t1, t2, fo):

    if fo = 0:  # fuel
        mProp = 38.5 # [kg]
    else:  # oxidixer
        mProp = 187.5 # [kg]

    mTank = (L * 2 * R * math.pi * t1 + 4 * math.pi * R * R * t2) * 

    return mTank + mProp
