"""
wninsd
------
Insert an interval into a double precision window

  left   : Left endpoints of new interval
  left   : Right endpoints of new interval
  window : Input window (must be declared as a double precision SpiceCell)


wnvald
------
Form a valid double precision window from the contents of a window array.

    :param insize: Size of window.
    :param n: Original number of endpoints.
    :param window: Input window.
    :return: The union of the intervals in the input cell.
"""


import spiceypy as sp
from datetime import datetime
import numpy as np

WINSIZ = 20
DATSIZ = 16

window = sp.stypes.SPICEDOUBLE_CELL(WINSIZ)
winData = sp.Cell_Double(DATSIZ)

#sp.furnsh('C:/Moi/_py/Astronomy/Solar System/kernels/naif0012.tls')


##los_et = np.array([sp.str2et(i) for i in los_rng])
##
##loswin = sp.stypes.SPICEDOUBLE_CELL( MAXSIZ )
##
##for i in los_et:
##    sp.wninsd(i[0], i[1], loswin)
##
##sp.wnvald( MAXSIZ, MAXSIZ, loswin )

#sp.kclear()
