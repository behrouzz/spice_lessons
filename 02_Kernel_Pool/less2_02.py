import spiceypy as sp

N_ITEMS =  20

sp.furnsh('kervar.tm')

START = 0
tmplate = '*RING*'

cvals = sp.gnpool( tmplate, START, N_ITEMS )



for cval in cvals:
    # Use spiceypy.dtpool to return the dimension and type,
    # C (character) or N (numeric), of each pool
    # variable name in the cvals array.
    dim, type = sp.dtpool(cval)
    print(cval)
    print(f'Number of items: {dim} of type: {type}\n')
    

sp.kclear()
