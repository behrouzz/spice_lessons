import spiceypy as sp

N_ITEMS =  20

sp.furnsh('kervar.tm')

START = 0
tmplate = '*RING*'

cvals = sp.gnpool( tmplate, START, N_ITEMS )



for cval in cvals:
    dim, type = sp.dtpool(cval)
    print(cval)
    print(f'Number of items: {dim} of type: {type}\n')
    
    # Test character equality, 'N' or 'C'.

    if type == 'N':
        
        # If 'type' equals 'N', we found a numeric array.
        # In this case any numeric array will be an array
        # of double precision numbers ('doubles').
        # spiceypy.gdpool retrieves doubles from the kernel pool.

        dvars = sp.gdpool(cval, START, N_ITEMS)
        for dvar in dvars:
            print('Numeric value:', dvar)

    elif type == 'C':

        # If 'type' equals 'C', we found a string array.
        # spiceypy.gcpool retrieves string values from the kernel pool.

        cvars = sp.gcpool(cval, START, N_ITEMS)

        for cvar in cvars:
            print('String value:', cvar)

    print('-'*50)


sp.kclear()
