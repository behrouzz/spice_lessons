import spiceypy as sp

sp.furnsh('xtic_h21.tm')

print(sp.str2et('2022-09-19 00:00:00'))
print(sp.str2et('2022-09-19 00:00:00 (UTC)'))
print(sp.str2et('2022-09-19 00:00:00 (TDB)'))

sp.kclear()

