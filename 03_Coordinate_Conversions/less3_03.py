import spiceypy as sp


INRFRM = 'J2000'
NONFRM = 'IAU_EARTH'
#NONFRM = 'ITRF93'
r2d = sp.dpr()

sp.furnsh('coord.tm')

timstr = '2002-02-03'
et = sp.str2et(timstr)

# Make the spiceypy.spkpos call to determine the apparent
# position of the Moon w.r.t. to the Earth at 'et' in the
# non-inertial, body fixed, frame.

pos, ltime = sp.spkpos('MOON', et, NONFRM, 'LT+S','EARTH')


print('Non-inertial Frame:', NONFRM)

# ...latitudinal coordinates...
rng, lon, lat = sp.reclat(pos)
"""
lon : angle between the prime meridian and the meridian containing the point
lat : angle from the XY plane of the ray from the origin through the point
"""

print('=== Latitudinal ===')
print('Rad  : {0:20.6f}'.format(rng))
print('Lon  : {0:20.6f}'.format(lon * r2d))
print('Lat  : {0:20.6f}'.format(lat * r2d))

# ...spherical coordinates...
rng, colat, lon = sp.recsph(pos)
"""
lon   : angle between the positive X-axis and the orthogonal projection
        of the point onto the XY plane.
        It increases in the counterclockwise sense about the positive Z-axis
colat : angle between the point and the positive Z-axis
"""

print('=== Spherical ===')
print('Rad  : {0:20.6f}'.format(rng))
print('Lon  : {0:20.6f}'.format(lon   * r2d))
print('Colat: {0:20.6f}'.format(colat * r2d))


# ...finally, convert the position to geodetic coordinates.
# =========================================================

# Access the kernel pool data for the triaxial radii of the
# Earth, rad[1][0] holds the equatorial radius, rad[1][2]
# the polar radius.
#
rad = sp.bodvrd( 'EARTH', 'RADII', 3 )

#
# Calculate the flattening factor for the Earth.
#
#          equatorial_radius - polar_radius
# flat =   ________________________________
#
#                equatorial_radius

flat = (rad[1][0] - rad[1][2])/rad[1][0]

# rectangular to geodetic
LON, LAT, ALT = sp.recgeo(pos, rad[1][0], flat)

"""
LON : geodetic longitude of the input point.
      This is the angle between the prime meridian and the meridian
      containing <pos>.
LAT : geodetic latitude of the input point.
      For a point P on the reference spheroid, this is the angle between
      the XY plane and the outward normal vector at P.
      For a point P not on the reference spheroid, the geodetic latitude
      is that of the closest point to P on the spheroid.
ALT : altitude of point above the reference spheroid.
      The units associated with ALT are those associated with <pos> and <RE>.
"""

print('=== Geodetic ===' )
print('ALT  : {0:20.6f}'.format(ALT))
print('LON  : {0:20.6f}'.format(LON * r2d))
print('LAT  : {0:20.6f}'.format(LAT * r2d))
print()


sp.kclear()

# Note the difference between the expression of latitude in
# the Latitudinal system and the corresponding Spherical colatitude:
#
# The spherical coordinate system uses the colatitude, the angle measure
# away from the positive Z axis. Latitude is the angle between the
# position vector and the x-y (equatorial) plane with positive angle
# defined as toward the positive Z direction
