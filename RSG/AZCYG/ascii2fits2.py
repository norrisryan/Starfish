def table2fits(tab, header=None):
    '''
        takes the data from an ascii.table.Table and outputs
        a pyfits.hdu.table.BinTableHDU, creating a blank
        header if no header is provided
    '''
    from astropy.io import fits
    if header is None:
        prihdr = fits.Header()
        prihdu = fits.PrimaryHDU(header=prihdr)
    else:
        prihdu = fits.PrimaryHDU(header=header)

    table_hdu = fits.BinTableHDU.from_columns(np.array(tab.filled()))

    return fits.HDUList([prihdu, table_hdu])

#scan directory for files

from astropy.table import Table
import glob
import numpy as np
dir="/home/norris/SOFTWARE/Starfish/libraries/raw/KURUCZ/T_03500"
filelist=glob.glob(dir+"/*ASC")
s=len(filelist)
for i in range(0, s):
    t = Table.read(filelist[i], format='ascii')
    newname = filelist[i].replace("ASC", "fits")
    t.write(newname, format='fits',overwrite=True)
    print("File: ", newname," Number: ",i)
print("Done")
