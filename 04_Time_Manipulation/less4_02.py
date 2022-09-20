import spiceypy as sp


CALSTR    = 'Mar 15, 2003 12:34:56.789 AM PST'

T_FORMAT1 = 'Wkd Mon DD HR:MN:SC PDT YYYY ::UTC-7'
T_FORMAT2 = 'Wkd Mon DD HR:MN ::UTC-7 YR (JULIAND.##### JDUTC)'


sp.furnsh('xtic_h21.tm')

et = sp.str2et(CALSTR)
print('Original time string :', CALSTR)
print('Corresponding ET     :',et)

timstr = sp.timout(et, T_FORMAT1)
print('Time in str format 1 :', timstr)

timstr = sp.timout(et, T_FORMAT2)
print('Time in str format 2 :', timstr)

sp.kclear()
