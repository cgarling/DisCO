from astropy.constants import h,c
import astropy.units as u
from math import pi
import numpy as np

"""
Computes <A(lambda)/A(V)> using Equations 1, 2, 3, and 4 from Cardelli et al., ApJ, 1989, Vol. 345. Call the function with a wavelength (with an associated astropy unit) and a value of Rv. For example, to calculate <A(lambda)/A(V)> at 2 microns with an Rv of 4, you would execute cardelli_law(2*u.um,4.0).
"""

def cardelli_law(wavelength, rv):
	#wavelength should have astropy units 
    	#wavenumber is the spectral wavenumber
        try: 
		if len(wavelength)>1:
                        if type(wavelength[0]) is not u.quantity.Quantity:wavelength=wavelength*u.um
			return_list=[]
			for i in range(len(wavelength)):
    				wavenumber=1.0/wavelength[i]
				wavenumber=wavenumber.to(1/u.um).value	
				if wavenumber>0.3 and wavenumber<1.1:
					return_list.append((0.574*wavenumber**1.61)+(-0.527*wavenumber**1.61)/rv)
				if wavenumber>1.1 and wavenumber<3.3:
					y=wavenumber-1.82
					return_list.append((1.0+0.17699*y-0.50447*y**2.-0.02427*y**3.+0.72085*y**4.+0.01979*y**5.-0.77530*y**6.+0.32999*y**7.)+(1.41338*y+2.28305*y**2.+1.07233*y**3.-5.38434*y**4.-0.62251*y**5.+5.30260*y**6.-2.09002*y**7.)/rv)

				if wavenumber>=3.3 and wavenumber<=8.0:
		        		if wavenumber>=5.9 and wavenumber<=8:
						F_a=-0.04473*(wavenumber-5.9)**2.-0.009779*(wavenumber-5.9)**3.
						F_b=0.2130*(wavenumber-5.9)**2.+0.1207*(wavenumber-5.9)**3.
					if wavenumber<5.9:
						F_a=0
						F_b=0
					return_list.append((1.752-0.316*wavenumber-0.104/((wavenumber-4.67)**2.+0.34)+F_a)+(-3.090+1.825*wavenumber+1.206/((wavenumber-4.62)**2.+0.263)+F_b)/rv)

			return np.array(return_list)

	except:
        	if type(wavelength) is not u.quantity.Quantity:wavelength=wavelength*u.um
        	wavenumber=1.0/wavelength
		wavenumber=wavenumber.to(1/u.um).value
		if wavenumber>=0.3 and wavenumber<1.1:
			return (0.574*wavenumber**1.61)+(-0.527*wavenumber**1.61)/rv
		if wavenumber>=1.1 and wavenumber<3.3:
			y=wavenumber-1.82
			return (1.0+0.17699*y-0.50447*y**2.-0.02427*y**3.+0.72085*y**4.+0.01979*y**5.-0.77530*y**6.+0.32999*y**7.)+(1.41338*y+2.28305*y**2.+1.07233*y**3.-5.38434*y**4.-0.62251*y**5.+5.30260*y**6.-2.09002*y**7.)/rv
		if wavenumber>=3.3 and wavenumber<=8.0:
		        if wavenumber>=5.9 and wavenumber<=8:
				F_a=-0.04473*(wavenumber-5.9)**2.-0.009779*(wavenumber-5.9)**3.
				F_b=0.2130*(wavenumber-5.9)**2.+0.1207*(wavenumber-5.9)**3.
			if wavenumber<5.9:
				F_a=0
				F_b=0
			return (1.752-0.316*wavenumber-0.104/((wavenumber-4.67)**2.+0.34)+F_a)+(-3.090+1.825*wavenumber+1.206/((wavenumber-4.62)**2.+0.263)+F_b)/rv


if __name__=='__main__':
	#plotting A(lambda)/A(V) as a test; compare to Figure 4 in Cardelli.
	import matplotlib.pyplot as plt
	print cardelli_law(1.11*u.um,4.0)
	plt.plot(1/np.linspace(0.15,2.0,500),cardelli_law(np.linspace(0.15,2.0,500),4.0))
	plt.show()
