#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dust_extinction.grain_models import D03
from dust_extinction.parameter_averages import G23

class ExtinctionLaw:
    """
    Represents an extinction law object that generates and saves the extinction law values.

    Attributes:
        Rv (float): The Rv value for the extinction law.
        wl (array-like): The wavelength values for which to generate the extinction law.
        N (int): The number of x values to generate if wl is not provided.
        G23_x_range (tuple): The x range for the G23 extinction law.
        D03_x_range (tuple): The x range for the D03 extinction law.
        x (array): The x values corresponding to the wavelength values.
        wavelength (array): The wavelength values for the extinction law.
        A_l_A_V (array): The extinction law values corresponding to the wavelength values.
    
    Methods:
        generate_extinction_law: Generates the extinction law for the given x values.
        save: Saves the extinction law to a csv file.
    
    Example of usage:
        extinction_law = ExtinctionLaw(Rv=3.1, wl=np.linspace(0.1, 10, num=1000))
        extinction_law.save(my_dir='./', filename='ExtinctionLaw_RV_3p1_D03_G23.csv')
    """

    def __init__(self, Rv=3.1, wl=None, N=1000):
        """
        Initializes an ExtinctionLaw object.

        Args:
            Rv (float, optional): The Rv value for the extinction law. Defaults to 3.1.
            wl (array-like, optional): The wavelength values for which to generate the extinction law.
            N (int, optional): The number of x values to generate if wl is not provided.
        """
        self.Rv = Rv
        self.G23_x_range = (1./12, 1./0.2)
        self.D03_x_range = D03.x_range
        if wl is None:
            self.x = np.logspace(np.log10(self.D03_x_range[0]), np.log10(self.D03_x_range[1]), num=N)
            self.wl = 1./self.x
        else:
            self.wl = np.atleast_1d(wl)
            self.x = 1./self.wl
        self.wavelength, self. A_l_A_V = self.generate_extinction_law()

    def generate_extinction_law(self):
        """
        Generates the extinction law for the given x values.

        Returns:
            tuple: The wavelength values and the extinction law values.
        """
        mask_G23 = (self.x >= self.G23_x_range[0]) & (self.x <= self.G23_x_range[1])
        mask_D03 = (self.x >= self.D03_x_range[0]) & (self.x <= self.D03_x_range[1])
        Av = np.full(len(self.x), np.nan)
        Av[mask_D03] = D03(modelname='MWRV31')(self.x[mask_D03])
        Av[mask_G23] = G23(Rv=self.Rv)(self.x[mask_G23])
        return 1./self.x, Av
    
    def save(self, my_dir='./', filename='ExtinctionLaw_RV_3p1_D03_G23.csv'):
        """
        Saves the extinction law to a csv file.

        Args:
            my_dir (str, optional): The directory to save the file in. Defaults to './'.
            filename (str, optional): The name of the file to save. Defaults to ''.
        """
        df = pd.DataFrame({'wavelength': self.wavelength, 'A_l_A_V': self.A_l_A_V})
        df.to_csv(my_dir + filename, index=False)
   