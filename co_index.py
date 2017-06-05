from scipy.integrate import trapz
import numpy as np


#index takes as arguments wavelength and flux vectors (numpy ndarrays) and computes the D_co index from Marmol-Queralto et al., 2008, A&A, 489.
#wavelengths must be in units of microns
#Index error computes the numerical error on the D_co value using Equation 10 of Marmol-Queralto 2008. Again, wavelength must be in microns.

def index(all_wavelength,all_flux):
	#currently only takes wavelengths in microns.
	#the index is a ratio of the average value of the continuum fluxes (in two different continuum regions) to the average value of absorbtion fluxes. We will compute the numerator and the denominator, then return the ratio.
	co_feature=[2.2880,2.3010]
	goodwave=all_wavelength[np.all((all_wavelength>co_feature[0],all_wavelength<co_feature[1]),axis=0)]
	goodflux=all_flux[np.all((all_wavelength>co_feature[0],all_wavelength<co_feature[1]),axis=0)]
	average_feature=trapz(goodflux,x=goodwave)/(co_feature[1]-co_feature[0])

	continuum1=[2.2460,2.2550]
	continuum2=[2.2710,2.2770]
	goodwave1=all_wavelength[np.all((all_wavelength>continuum1[0],all_wavelength<continuum1[1]),axis=0)]
	goodflux1=all_flux[np.all((all_wavelength>continuum1[0],all_wavelength<continuum1[1]),axis=0)]
	goodwave2=all_wavelength[np.all((all_wavelength>continuum2[0],all_wavelength<continuum2[1]),axis=0)]
	goodflux2=all_flux[np.all((all_wavelength>continuum2[0],all_wavelength<continuum2[1]),axis=0)]
	average_continuum=(trapz(goodflux1,x=goodwave1)+trapz(goodflux2,x=goodwave2))/((continuum1[1]-continuum1[0])+(continuum2[1]-continuum2[0]))
	return average_continuum/average_feature
	

def index_error(all_wavelength,all_flux,all_error):
	co_feature=[2.2880,2.3010]
	goodwave=all_wavelength[np.all((all_wavelength>co_feature[0],all_wavelength<co_feature[1]),axis=0)]
	goodflux=all_flux[np.all((all_wavelength>co_feature[0],all_wavelength<co_feature[1]),axis=0)]
	gooderr=all_error[np.all((all_wavelength>co_feature[0],all_wavelength<co_feature[1]),axis=0)]
	F_a=np.sum(goodflux)/(co_feature[1]-co_feature[0])
	sigma_a=np.sum(gooderr)/(co_feature[1]-co_feature[0])

	continuum1=[2.2460,2.2550]
	continuum2=[2.2710,2.2770]
	goodwave1=all_wavelength[np.all((all_wavelength>continuum1[0],all_wavelength<continuum1[1]),axis=0)]
	goodflux1=all_flux[np.all((all_wavelength>continuum1[0],all_wavelength<continuum1[1]),axis=0)]
	gooderr1=all_error[np.all((all_wavelength>continuum1[0],all_wavelength<continuum1[1]),axis=0)]
	goodwave2=all_wavelength[np.all((all_wavelength>continuum2[0],all_wavelength<continuum2[1]),axis=0)]
	goodflux2=all_flux[np.all((all_wavelength>continuum2[0],all_wavelength<continuum2[1]),axis=0)]
	gooderr2=all_error[np.all((all_wavelength>continuum2[0],all_wavelength<continuum2[1]),axis=0)]
	F_c=(np.sum(goodflux1)+np.sum(goodflux2))/((continuum1[1]-continuum1[0])+(continuum2[1]-continuum2[0]))
	sigma_c=(np.sum(gooderr1)+np.sum(gooderr2))/((continuum1[1]-continuum1[0])+(continuum2[1]-continuum2[0]))
	return np.sqrt((F_c**2*sigma_a**2 + F_a**2*sigma_c**2)/(F_a**4))

if __name__ == '__main__':
        import urllib2
        import matplotlib.pyplot as plt
        # import the file from SpeX library
        file = urllib2.urlopen('http://irtfweb.ifa.hawaii.edu/~spex/IRTF_Spectral_Library/Data/K0III_HD100006.txt')
        wavelength, flux_density, flux_density_error=np.loadtxt(file,unpack=True,dtype='f,f,f')
        wavelength=wavelength[flux_density!=-999]
        flux_density=flux_density[flux_density!=-999]
        flux_density_error=flux_density_error[flux_density!=-999]
        # convert to flux from flux density
        flux=flux_density*wavelength
        flux_error=flux_density_error*wavelength
        # calculate the index and the index error
        index_val = index(wavelength,flux)
        index_val_error = index_error(wavelength,flux,flux_error)
        plt.plot(wavelength,flux,c='b')
        plt.title("D$_{CO}$ = "+str(index_val)+' $\pm$ '+str(index_val_error))
        plt.xlabel('$\mu m$')
        plt.ylabel('W / $m^2$')
        plt.show()
