
if __name__ == "__main__":
	import os
	import urllib2
	import numpy as np

	#script will download two of the SpeX IRTF library spectra in text form and show you how to use the functions in the package.

	#downloading the data
	if os.path.isfile('K0III.txt')==False:
		response=urllib2.urlopen('http://irtfweb.ifa.hawaii.edu/~spex/IRTF_Spectral_Library/Data/K0III_HD100006.txt')
		html=response.read()
		open('K0III.txt','w').write(html)
	if os.path.isfile('K5III.txt')==False:
		response=urllib2.urlopen('http://irtfweb.ifa.hawaii.edu/~spex/IRTF_Spectral_Library/Data/K5III_HD181596.txt')
		html=response.read()
		open('K5III.txt','w').write(html)

        wave1, flux1, flux_err1=np.loadtxt('K0III.txt',unpack=True,dtype='f,f,f')


