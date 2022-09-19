KPL/MK

   Define the paths to the kernel directory. Use the PATH_SYMBOLS
   as aliases to the paths.

   The names and contents of the kernels referenced by this
   meta-kernel are as follows:

      File Name        Description
      ---------------  ------------------------------
      naif0012.tls     Generic LSK.
      de440s.bsp       Planet Ephemeris SPK.
      pck00010.tpc     Generic PCK.


\begindata

   PATH_VALUES     = ( 'C:/Moi/_py/Astronomy/Solar System/kernels' )

   PATH_SYMBOLS    = ( 'KKK' )

   KERNELS_TO_LOAD = ( '$KKK/naif0012.tls',
                       '$KKK/de440s.bsp',
                       '$KKK/pck00010.tpc' )

\begintext