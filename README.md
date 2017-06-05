
[comment]: # (co_work)
### Code relating to analysis of the CO absorption feature at 2.3 microns

**co_index.py** contains functions to evaluate the D<sub>CO</sub> index of Marmol-Queralto et al., 2008, A&A, 489 (<http://adsabs.harvard.edu/abs/2008A%26A...489..885M>). Requires Scipy and Numpy. If you'd like to run the file, it will grab data from a K0III star from the SpeX IRTF Library (Rayner et al. 2009), plot it using Matplotlib, and compute the value of the D<sub>CO</sub> index and its numerical uncertainty.

  * index(wavelength, flux)
    * Takes numpy ndarrays of wavelength (in microns only) and flux and evaluates the D<sub>CO</sub> index, returning a float.
  
  * index_error(wavelength, flux, flux_error)
    * Takes numpy ndarrays of wavelength (in microns only), flux, and flux errors and evaluates the numerical error on the D<sub>CO</sub> value using Equation 10 of Marmol-Queralto et al. (2008).

**CO_fitting_funcs.py** contains the fitting equations of Marmol-Queralto et al. (2008). Requires Numpy.

These equations should be used by calling the function co_fitting(theta,logg,feh,agb=False), with the arguments
  * theta: 5040 K / T<sub>eff</sub>
  * logg: logarithm of the surface gravity of your star. This is used to distinguish between the equations calibrated for giants and dwarfs; an exact value is not needed. If you know your star is a giant, logg=2.5 is a good value, and for dwarfs, I recommend logg=4.5.
  * feh: The iron abundace [Fe/H] for your star. These do factor into the fitting equations, so if you are unsure of the iron abundance of your star, estimating an [Fe/H] will usually introduce uncertainty. 
  * agb: Marmol-Queralto et al. (2008) calibrated a fitting equation explicitly for AGB stars. If your star is on the AGB, you should set agb=True. The default is False.

The function will return the value of the D<sub>CO</sub> index for a star with the properties you input.

**co_extinction.py** contains convenience functions for reddening/dereddening and finding extinction as a function of wavelength for the Boogert et al. 2011 (<http://adsabs.harvard.edu/abs/2011ApJ...729...92B> and Indebetouw et al. 2005 (<http://adsabs.harvard.edu/abs/2005ApJ...619..931I>) laws. Requires Numpy.

**cardelli_convert.py** contains a function, cardelli_law, which will compute <img src="http://i.imgur.com/uvw4SdL.png" height="20"> for a given wavelength using Equations 1, 2, 3, and 4 from Cardelli et al. 1989 (<http://adsabs.harvard.edu/abs/1989ApJ...345..245C>). If the wavelength you input to the function is not in microns, you must specify its units using astropy units. You can input an integer or float if your input is in microns. Requires Numpy and Astropy. If you'd like to run the file, it will plot the extinction curve (Figure 4 from Cardelli et al. 1989) using Matplotlib.


