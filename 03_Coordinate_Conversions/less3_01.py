import spiceypy as sp


INRFRM = 'J2000'
NONFRM = 'IAU_EARTH'
r2d = sp.dpr()

sp.furnsh('coord.tm')

timstr = '2002-02-03'
et = sp.str2et(timstr)

# apparent position of the Moon wrt Earth at 'et' in the inertial frame
    
pos, ltime = sp.spkpos('MOON', et, INRFRM, 'LT+S', 'EARTH')

# Show the current frame and time.
print('Time :', timstr)
print('Inertial Frame:', INRFRM)
print(pos)
print(ltime)

sp.kclear()
