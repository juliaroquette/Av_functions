**@juliaroquette - 20 December 2023** This repository concentrates on functions related to the extinction law. 

# The extinction Law itself
In [ExtinctionLaw.ipynb](https://github.com/juliaroquette/Av_functions/blob/main/ExtinctionLaw.ipynb) I am testing a few different extinction laws and choosing a combination of literature extinction 
laws as default. These are basically development notes behind the class [ExtinctionLaw](https://github.com/juliaroquette/Av_functions/blob/main/extinction_law.py), which can be used to interpolate 
values of $\frac{A_\lambda}{A_V}$ for any $\lambda$ from 0.0001 -- 10000$\mu$m. 

This is done employing the [`dust_extinction`](https://dust-extinction.readthedocs.io/en/stable/index.html) package from AstroPy. My current default extinction curve has the following assumptions:

1. $R_V=3.1$ - although in the future I may want to escalate this for other values of $R_V$. 
2. For the range 0.2-12$\mu$m, I am adopting the  [Gordon et al. 2023](https://ui.adsabs.harvard.edu/abs/2023ApJ...950...86G/abstract) extinction law.
3. Outside this range, I am adopting an extinction law from dust-models by [Draine (2003, ARA&A, 41, 241; 2003, ApJ, 598, 1017)](https://ui.adsabs.harvard.edu/abs/2003ARA%26A..41..241D/abstract), who used the distribution of grains sizes from  [Weingartner & Draine (2001, ApJ, 548, 296)](https://ui.adsabs.harvard.edu/abs/2001ApJ...548..296W/abstract).
4. The truncation limits in 2. are chosen by eye based on the comparison between the extinction curves in 2. and 3.. 
5. The upper and lower limit is defined by the availability of 3. 
6. This extinction law is valid for the Milky Way.

TO DO: In the future this package will also allow deriving $A_\lambda$ for a given photometric system given a transmission curve. 

# Extinction derivations using the T-Tauri Locus

The jupyter-notebook [get_Av_from_JHK_TTauriLocus.ipynb](https://github.com/juliaroquette/Av_functions/blob/main/get_Av_from_JHK_TTauriLocus.ipynb) contains notes of the development of a code to estimate $A_V$ values 
for Young Stellar Objects (YSO) based on the JHKs-colour space using the Classical TTauri Locus as a reference. 
