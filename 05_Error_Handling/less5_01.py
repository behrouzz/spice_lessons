import spiceypy as sp
from spiceypy.utils.support_types import SpiceyError
from datetime import datetime

t = datetime.utcnow()

SPICETRUE = True
SPICEFALSE = False
doloop = SPICETRUE

adr = 'C:/Users/H21/Desktop/Desktop/Behrouz/Astronomy/kernels/'
kernels = [adr+'naif0012.tls', adr+'de440s.bsp']


for k in kernels:
    sp.furnsh(k)

et = sp.str2et(str(t))

while (doloop):
    targ = input('Target: ')
    if targ == 'NONE':
        doloop = SPICEFALSE
    else:
        try:
            state, lt = sp.spkezr(targ, et, 'J2000', 'LT+S', 'EARTH')
            print('POS:', state[:3])
            print('VEL:', state[3:])
            print('LT :', lt)
            print('\n')
        except SpiceyError as err:
            print('\n', err, '\n')

sp.kclear()
