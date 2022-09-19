import spiceypy as sp

META = 'kpool.tm'

# Load the meta kernel
sp.furnsh(META)

# use KTOTAL to interrogate the SPICE kernel subsystem
count = sp.ktotal('ALL')
print('Kernel count after load:', count)


# Loop over the number of files; interrogate the SPICE system
# with spiceypy.kdata for the kernel names and the type.
# 'found' returns a boolean indicating whether any kernel files
# of the specified type were loaded by the kernel subsystem.
# This example ignores checking 'found' as kernels are known
# to be loaded.

for i in range(count):
    file, type, source, handle = sp.kdata(i, 'ALL')
    print('File   :', file)
    print('Type   :', type)
    print('Source :', source)

print('=======================================')

# Unload one kernel then check the count.
sp.unload('C:/Users/H21/Desktop/Desktop/Behrouz/Astronomy/kernels/de440s.bsp')
count = sp.ktotal('ALL')

# The subsystem should report one less kernel.
print( 'Kernel count after one unload:', count)

# Now unload the meta kernel. This action unloads all files
sp.unload(META)


# Check the count; spiceypy should return a count of zero.
count = sp.ktotal('ALL')
print( 'Kernel count after meta unload:', count)

# Done. Unload the kernels.
sp.kclear()
