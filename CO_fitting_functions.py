import numpy as np

#	Purpose: This code will take temperature, surface gravity, iron abundance, and asymptotic giant branch information and use the fitting functions from Marmol-Queralto et al. 2008 to produce a D_co index value.
#	Usage: the user-level function here is co_fitting, which in turn relies on the rest of the functions.
#	Syntax: co_fitting(theta,logg,feh,agb=False)
#	Theta: Float. Effective temperature divided by 5040 K.
#	logg: Float. The logarithm of the surface gravity.
#	feh: Float. The iron abundance [Fe/H].
#	agb: Boolean. Is the star on the asymptotic giant branch? If yes, use special fitting function.

#setting up each of the functions we'll be using in different regions of temperature 
def hot_dwarfs(theta,logg,feh):
	c0=0.0499
	return np.exp(c0)

def agb_star(theta,logg,feh):
	c0=-0.8893
	theta1=1.4950
	theta2=-0.4816
	return np.exp(c0+theta*theta1+(theta**2*theta2))

def cool_dwarfs(theta,logg,feh):
	c0=-0.0292
	theta1=0.1006
	feh1=0.0174
	return np.exp(c0+theta*theta1+feh*feh1)

def cold_dwarfs(theta,logg,feh):
	c0=0.1025
	return np.exp(c0)

def hot_giants(theta,logg,feh):
	c0=0.0459
	return np.exp(c0)

def warm_giants(theta,logg,feh):
    	c0=-0.3073
	theta1=0.3876
	feh1=-0.1016
	theta_feh=0.1072
	feh2=-0.0023
        return np.exp(c0+theta1*theta+feh1*feh+(theta*feh*theta_feh)+feh2*feh**2)

def cool_giants(theta,logg,feh):
	c0=-0.5224
	theta1=0.8257
	feh1=0.0674
	theta_feh=-0.0444
	theta2=-0.2200
	feh2=-0.0023
	return np.exp(c0+theta*theta1+feh*feh1+(theta*feh*theta_feh)+(theta2*theta**2)+feh2*feh**2)

def cold_giants(theta,logg,feh):
	c0=0.2397
	return np.exp(c0)



######################################################################

#actual function to call to evaluate the index
def co_fitting(theta,logg,feh,agb=False):
    if agb==True:
	return agb_star(theta,logg,feh)


    if theta >= 0.38 and theta < 0.80 and logg >= 3.50 and logg <= 5.50:
	return hot_dwarfs(theta,logg,feh)

    elif theta >= 0.80 and theta <= 0.90 and logg >= 3.50 and logg <= 5.50:
	#intersection between hot dwarfs and cool dwarfs, cosine weighted mean
	hotdwarfs=[0.38,0.90]		#this is I1
        cooldwarfs=[0.80,1.50]		#this is I2
	weight1=(theta-cooldwarfs[0])/(hotdwarfs[1]-cooldwarfs[0])
	weight=np.cos((np.pi/2.0)*(weight1))
	return weight*hot_dwarfs(theta,logg,feh)+(1-weight)*cool_dwarfs(theta,logg,feh)


    elif theta > 0.90 and theta < 1.45 and logg >= 3.50 and logg <= 5.50:
	return cool_dwarfs(theta,logg,feh)


    elif theta >= 1.45 and theta<=1.50 and logg >= 3.50 and logg <= 5.50:
	#intersection between cool dwarfs and cold dwarfs, cosine weighted mean
	cooldwarfs=[0.80,1.50]		#this is I1
        colddwarfs=[1.33,1.80]		#this is I2
	weight1=(theta-colddwarfs[0])/(cooldwarfs[1]-colddwarfs[0])
	weight=np.cos((np.pi/2.0)*(weight1))
	return weight*cool_dwarfs(theta,logg,feh)+(1-weight)*cold_dwarfs(theta,logg,feh)


    elif theta >= 1.50 and theta <= 1.80 and logg >= 3.80 and logg <= 5.50:
	return cold_dwarfs(theta,logg,feh)

    elif theta >= 0.42 and theta < 0.90 and logg >= -0.40 and logg <= 3.50:
	return hot_giants(theta,logg,feh)

    elif theta >= 0.90 and theta <= 0.93 and logg >= -0.40 and logg <= 3.50:
    #intersection between hot giants and warm giants, cosine weighted mean
        hotgiants=[0.42,0.91]		#this is I1
        warmgiants=[0.90,1.131]		#this is I2
	weight1=(theta-warmgiants[0])/(hotgiants[1]-warmgiants[0])
	weight=np.cos((np.pi/2.0)*(weight1))
	return weight*hot_giants(theta,logg,feh)+(1-weight)*warm_giants(theta,logg,feh)


    elif 0.93 < theta and theta < 1.09 and logg >= 0.13 and logg <= 3.5:
	return warm_giants(theta,logg,feh)

    elif 1.09 <= theta and 1.10 >= theta and logg >= 0.13 and logg <= 3.5:
    #intersection between warm giants and cool giants, distance weighted mean
	warmgiants=[0.90,1.131]		#this is I1
        coolgiants=[1.10,1.60]		#this is I2
	weight=(theta-coolgiants[0])/(warmgiants[1]-coolgiants[0])
	return weight*warm_giants(theta,logg,feh)+(1-weight)*cool_giants(theta,logg,feh)
	

    elif theta > 1.10 and theta <= 1.60 and logg >= -0.34 and logg <= 3.41:
	return cool_giants(theta,logg,feh)

    elif theta >= 1.55 and theta <= 2.03 and logg >= -0.07 and logg <= 3.50:
	return cold_giants(theta,logg,feh)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    #randomly sample temperature, fe/h and plot the results
    #constant logg=1.5
    numpoints=1000
    np.random.seed(3)

    theta=(np.random.randn(numpoints)+1.3)*0.8
    #logg=(np.random.randn(numpoints)+2.5)
    logg=np.zeros(numpoints)+1.50
    feh=np.random.randn(numpoints)

    indices=[]
    for i in range(len(theta)):
	indices.append(co_fitting(theta[i],logg[i],feh[i]))

    fig=plt.figure()
    ax1=plt.subplot(111)
    ax1.text(0.6,0.95,'[Fe/H] Dependence, log($g$)=1.50',transform=fig.transFigure)
    points=ax1.scatter(theta,indices,c=feh,cmap='gist_ncar')
    ax1.set_xlabel(r'$\theta$=(5040/T$_\mathrm{eff})$')
    ax1.set_ylabel('D$_\mathrm{CO}$')
    ax1.set_xlim([0.4,2.0])
    fig.colorbar(points)

    ax2=ax1.twiny()
    new_xticks=[]
    for i in ax1.get_xticks():
	new_xticks.append(str(5040./i).split('.',1)[0])
    ax2.set_xlim(ax1.get_xlim())
    ax2.set_xticks(ax1.get_xticks())
    ax2.set_xticklabels(new_xticks)
    ax2.set_xlabel(r'T$_\mathrm{eff}$ (K)')
    plt.show(fig)
    plt.close(fig)
