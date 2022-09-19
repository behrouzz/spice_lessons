import spiceypy as sp
from spiceypy.utils.support_types import SpiceyError


# Define max number of kernel variables of concern for this examples
N_ITEMS =  20

sp.furnsh('kervar.tm')

# Initialize the start value. This value indicates
# index of the first element to return if a kernel
# variable is an array. START = 0 indicates return everything.
# START = 1 indicates return everything but the first element.
START = 0

# Set the template for the variable names to find. Let's
# look for all variables containing  the string RING.
# Define this with the wildcard template '*RING*'. Note:
# the template '*RING' would match any variable name
# ending with the RING string.
tmplate = '*RING*'

# We're ready to interrogate the kernel pool for the
# variables matching the template. spiceypy.gnpool tells us:
#
#  1. Does the kernel pool contain any variables that
#     match the template (value of found).
#  2. If so, how many variables?
#  3. The variable names. (cvals, an array of strings)

try:
    cvals = sp.gnpool( tmplate, START, N_ITEMS )
    print('Number variables matching template:', len(cvals), '\n')
    print('Variable names:\n', cvals)
    
except SpiceyError:
    print('No kernel variables matched template.')
    #return ????

sp.kclear()
