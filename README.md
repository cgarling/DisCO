
[comment]: # (co_work)
### Code relating to analysis of the CO absorption feature at 2.3 microns

co_index.py contains functions to evaluate the D<sub>CO</sub> index of Marmol-Queralto et al., 2008, A&A, 489. 

  * index(wavelength, flux)
    * Takes numpy ndarrays of wavelength (in microns only) and flux and evaluates the D<sub>CO</sub> index, returning a float.
  
  * index_error(wavelength, flux, flux_error)
    * Takes numpy ndarrays of wavelength (in microns only), flux, and flux errors and evaluates the numerical error on the D<sub>CO</sub> value using Equation 10 of Marmol-Queralto et al. (2008).
