import Starfish
from Starfish.grid_tools import KuruczGridInterfaceRN as ATLAS
import numpy as np
mygrid = ATLAS()
my_params = np.array([3750, 0.0, 0.0])
flux, hdr = mygrid.load_flux(my_params)
