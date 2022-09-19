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

    if type == 'N':
        dvars = sp.gdpool(cval, START, N_ITEMS)
        for dvar in dvars:
            print('Numeric value:', dvar)

    elif type == 'C':
        cvars = sp.gcpool(cval, START, N_ITEMS)
        for cvar in cvars:
            print('String value:', cvar)

    print('-'*50)




# Now look at the time variable EXAMPLE_TIMES.
# Extract this value as an array of doubles.
dvars = sp.gdpool('EXAMPLE_TIMES', START, N_ITEMS)

print('EXAMPLE_TIMES')

for dvar in dvars:
    print('  Time value:    {0:20.6f}'.format(dvar))



sp.kclear()
