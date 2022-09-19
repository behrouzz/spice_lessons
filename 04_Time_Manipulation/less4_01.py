import spiceypy as sp


CALSTR    = 'Mar 15, 2003 12:34:56.789 AM PST'
AMBIGSTR  = 'Mar 15, 79 12:34:56'
T_FORMAT1 = 'Wkd Mon DD HR:MN:SC PDT YYYY ::UTC-7'
T_FORMAT2 = 'Wkd Mon DD HR:MN ::UTC-7 YR (JULIAND.##### JDUTC)'


sp.furnsh('xtic.tm')

et = sp.str2et(CALSTR)
print( 'Original time string :', CALSTR)
print( 'Corresponding ET     :',et)

print(sp.str2et('2022-09-19 00:00:00'))
print(sp.str2et('2022-09-19 00:00:00 (UTC)'))
print(sp.str2et('2022-09-19 00:00:00 (TDB)'))

sp.kclear()
