import spiceypy as sp


INRFRM = 'J2000'
NONFRM = 'IAU_EARTH'
r2d = sp.dpr()

sp.furnsh('coord.tm')


timstr = '2002-02-03'
et = sp.str2et(timstr)

# rectangular coordinates
pos, ltime = sp.spkpos('MOON', et, INRFRM, 'LT+S', 'EARTH')


# Convert rectangular to range, Ra, Dec
rng, ra, dec = sp.recrad(pos)

print('=== Range/Ra/Dec ===')
print('Range: {0:20.6f}'.format(rng))
print('RA   : {0:20.6f}'.format(ra * r2d))
print('DEC  : {0:20.6f}'.format(dec* r2d))

# Convert rectangular to latitudinal (Range, Lon, Lat)
rng, lon, lat = sp.reclat(pos)

print('=== Latitudinal ===')
print('Rad  : {0:20.6f}'.format(rng))
print('Lon  : {0:20.6f}'.format(lon * r2d))
print('Lat  : {0:20.6f}'.format(lat * r2d))

# Convert rectangular to spherical
# (spherical coords use the colatitude, the angle from the Z axis)
rng, colat, lon = sp.recsph(pos)

print( '=== Spherical ===' )
print('Rad  : {0:20.6f}'.format(rng))
print('Lon  : {0:20.6f}'.format(lon   * r2d))
print('Colat: {0:20.6f}'.format(colat * r2d))


sp.kclear()
