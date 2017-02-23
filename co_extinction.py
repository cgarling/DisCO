import numpy as np

def deredden(flux_o,a_lambda):
	#take a flux and deredden it by the extinction value a_lambda (in magnitudes at wavelength lambda).
	return flux_o*10.**(0.4*a_lambda)

def redden(flux_o,a_lambda):
	#take a flux and redden it by the extinction value a_lambda (in magnitudes at wavelength lambda).
	return flux_o*10.**(-0.4*a_lambda)

def boogert_extinct(a_k,wavelength):
	#use the extinction law from Boogert et al. 2011 to formulate the extinction at the input wavelength (input in microns).
	#a_k is the K band extinction in magnitudes, wavelength is the array of wavelength in microns.
	a0=0.5924
	a1=-1.8235
	a2=-1.3020
	a3=5.9936
	a4=-5.3429
	a5=1.2619
	a6=0.2738
	a7=0.0069
	a8=-0.0554
	return a_k*10**(a0+a1*np.log10(wavelength)+a2*(np.log10(wavelength)**2)+a3*(np.log10(wavelength)**3)+a4*(np.log10(wavelength)**4)+a5*(np.log10(wavelength)**5)+a6*(np.log10(wavelength)**6)+a7*(np.log10(wavelength)**7)+a8*(np.log10(wavelength)**8))

def indebetouw_extinct(a_k,wavelength):
        #use the extinction law from Indebetouw et al. 2005 to formulate the extinction at the input wavelength (input in microns).
	a0=0.61
        a1=-2.22
	a2=1.21
	return a_k*10**(a0+a1*np.log10(wavelength)+a2*(np.log10(wavelength)**2))
