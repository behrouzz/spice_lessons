import spiceypy as sp


CALSTR    = 'Mar 15, 2003 12:34:56.789 AM PST'

sp.furnsh('xtic_h21.tm')

et = sp.str2et(CALSTR)

pic = '12:34:56.789 P.M. PDT January 1, 2006'
pictr, ok, xerror = sp.tpictr(pic)

if not bool(ok):
    print(xerror)
    exit


timstr = sp.timout(et, pictr)
print('Time in string format 3 :', timstr)

sp.kclear()
