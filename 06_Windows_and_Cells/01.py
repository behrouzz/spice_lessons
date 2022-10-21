"""
wninsd
------
Insert an interval into a double precision window

  left   : Left endpoints of new interval
  left   : Right endpoints of new interval
  window : Input window (must be declared as a double precision SpiceCell)
"""


import spiceypy as sp
from datetime import datetime
import numpy as np

MAXSIZ = 8

# Define a set of time intervals. For the purposes of this
# tutorial program, define time intervals representing
# an unobscured line of sight between a ground station
# and some body.


los_rng = [['Jan 1, 2003 22:15:02', 'Jan 2, 2003  4:43:29'],
           ['Jan 2, 2003  4:43:29', 'Jan 4, 2003  9:55:30'],
           ['Jan 4, 2003  9:55:30', 'Jan 4, 2003 11:26:52'],
           ['Jan 4, 2003 11:26:52', 'Jan 5, 2003 11:09:17'],
           ['Jan 5, 2003 11:09:17', 'Jan 5, 2003 13:00:41'],
           ['Jan 5, 2003 13:00:41', 'Jan 6, 2003 00:08:13'],
           ['Jan 6, 2003 00:08:13', 'Jan 6, 2003  2:18:01']]



# A second set of intervals representing the times for which
# an acceptable phase angle exists between the ground station,
# the body and the Sun.


phase_rng = [['Jan 2, 2003 00:03:30', 'Jan 2, 2003 19:00:00'],
             ['Jan 2, 2003 19:00:00', 'Jan 3, 2003  8:00:00'],
             ['Jan 3, 2003  8:00:00', 'Jan 3, 2003  9:50:00'],
             ['Jan 3, 2003  9:50:00', 'Jan 5, 2003 12:00:00'],
             ['Jan 5, 2003 12:00:00', 'Jan 5, 2003 12:45:00'],
             ['Jan 5, 2003 12:45:00', 'Jan 6, 2003 00:30:00'],
             ['Jan 6, 2003 00:30:00', 'Jan 6, 2003 23:00:00']]




# Load our meta kernel for the leapseconds data.
sp.furnsh('C:/Moi/_py/Astronomy/Solar System/kernels/naif0012.tls')


# SPICE windows consist of double precision values.
# Convert the string time tags defined in the 'los' and 'phase'
# arrays to double precision ET.
# Store the double values in the 'loswin' and 'phswin' windows.

los_et = np.array([sp.str2et(i) for i in los_rng])
phs_et = np.array([sp.str2et(i) for i in phase_rng])


loswin = sp.stypes.SPICEDOUBLE_CELL( MAXSIZ )
phswin = sp.stypes.SPICEDOUBLE_CELL( MAXSIZ )


for i in los_et:
    sp.wninsd(i[0], i[1], loswin)

for i in phs_et:
    sp.wninsd(i[0], i[1], phswin)


sp.wnvald( MAXSIZ, MAXSIZ, loswin )
sp.wnvald( MAXSIZ, MAXSIZ, phswin )


sp.kclear()
