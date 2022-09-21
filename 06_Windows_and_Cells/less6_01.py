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


MAXSIZ = 8

# Define a set of time intervals. For the purposes of this
# tutorial program, define time intervals representing
# an unobscured line of sight between a ground station
# and some body.

los = [ 'Jan 1, 2003 22:15:02', 'Jan 2, 2003  4:43:29',
        'Jan 4, 2003  9:55:30', 'Jan 4, 2003 11:26:52',
        'Jan 5, 2003 11:09:17', 'Jan 5, 2003 13:00:41',
        'Jan 6, 2003 00:08:13', 'Jan 6, 2003  2:18:01' ]

# A second set of intervals representing the times for which
# an acceptable phase angle exists between the ground station,
# the body and the Sun.

phase = [ 'Jan 2, 2003 00:03:30', 'Jan 2, 2003 19:00:00',
          'Jan 3, 2003  8:00:00', 'Jan 3, 2003  9:50:00',
          'Jan 5, 2003 12:00:00', 'Jan 5, 2003 12:45:00',
          'Jan 6, 2003 00:30:00', 'Jan 6, 2003 23:00:00' ]


# Load our meta kernel for the leapseconds data.
sp.furnsh( 'C:/Users/H21/Desktop/Desktop/Behrouz/Astronomy/kernels/naif0012.tls')


# SPICE windows consist of double precision values.
# Convert the string time tags defined in the 'los' and 'phase'
# arrays to double precision ET.
# Store the double values in the 'loswin' and 'phswin' windows.

los_et = sp.str2et(los)
phs_et = sp.str2et(phase)

loswin = sp.stypes.SPICEDOUBLE_CELL( MAXSIZ )
phswin = sp.stypes.SPICEDOUBLE_CELL( MAXSIZ )

for i in range(int(MAXSIZ/2)):
    sp.wninsd( los_et[2*i], los_et[2*i+1], loswin )
    sp.wninsd( phs_et[2*i], phs_et[2*i+1], phswin )

sp.wnvald( MAXSIZ, MAXSIZ, loswin )
sp.wnvald( MAXSIZ, MAXSIZ, phswin )

# The issue for consideration, at what times do line of
# sight events coincide with acceptable phase angles?
# Perform the set operation AND on loswin, phswin,
# (the intersection of the time intervals)
# place the results in the window 'sched'.

sched = sp.wnintd( loswin, phswin )

print( 'Number data values in sched : '
       '{0:2d}'.format(sp.card(sched)) )

#
# Output the results. The number of intervals in 'sched'
# is half the number of data points (the cardinality).
#
print( ' ' )
print( 'Time intervals meeting defined criterion.' )

for i in range( sp.card(sched)//2):

   #
   # Extract from the derived 'sched' the values defining the
   # time intervals.
   #
   [left, right ] = sp.wnfetd( sched, i )

   #
   # Convert the ET values to UTC for human comprehension.
   #
   utcstr_l = sp.et2utc( left , 'C', 3 )
   utcstr_r = sp.et2utc( right, 'C', 3 )

   #
   # Output the UTC string and the corresponding index
   # for the interval.
   #
   print( '{0:2d}   {1}   {2}'.format(i, utcstr_l, utcstr_r))


#
# Summarize the 'sched' window.
#
[meas, avg, stddev, small, large] = sp.wnsumd( sched )

print( '\nSummary of sched window\n' )

print( 'o Total measure of sched    : {0:16.6f}'.format(meas))
print( 'o Average measure of sched  : {0:16.6f}'.format(avg))
print( 'o Standard deviation of ' )
print( '  the measures in sched     : '
       '{0:16.6f}'.format(stddev))

#
# The values for small and large refer to the indexes of the
# values in the window ('sched'). The shortest interval is
#
#      [ sched.base[ sched.data + small]
#        sched.base[ sched.data + small +1]  ];
#
# the longest is
#
#      [ sched.base[ sched.data + large]
#        sched.base[ sched.data + large +1]  ];
#
# Output the interval indexes for the shortest and longest
# intervals. As Python bases an array index on 0, the interval
# index is half the array index.
#
print( 'o Index of shortest interval: '
       '{0:2d}'.format(int(small/2)) )
print( 'o Index of longest interval : '
       '{0:2d}'.format(int(large/2)) )




sp.kclear()
