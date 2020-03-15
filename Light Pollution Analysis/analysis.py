import matplotlib.pyplot as plt
import cv2
from PIL import Image
import pandas as pd
import numpy as np
from skimage import measure
from skimage import data, feature, exposure
from astropy.stats import sigma_clipped_stats
import glob


#################################
qe = 0.84
exp = 10
r = 0.08
pixel = 2.4e-6
pi = np.pi
focalLength = 0.35
platescale = 206265/focalLength
platescale_pixelsize = (platescale*pixel)**2
#################################

image_path = (r"C:\Users\veron\OneDrive\Desktop\Images_Paul\Analysis Data\Aldebaran_41\11pm_aldebaran-filter790_5ms")
directories = glob.glob(f"{image_path}/*.png")

darks_path = (r"C:\Users\veron\OneDrive\Desktop\Images_Paul\Analysis Data\Darks\Dark-filter790_5ms")
darks = glob.glob(f"{darks_path}/*.png")

for image, dark in zip(directories, darks):

    img = cv2.imread(image, 0)
    dark = cv2.imread(dark, 0)

    # Dark subtraction
    dark_sub = cv2.subtract(img, dark)

    xc = 2586
    yc = 2236
    rad = 80

    # plt.imshow(dark_sub)
    x1 = xc - rad
    x2 = xc + rad
    y1 = yc - rad
    y2 = yc + rad

    mask = dark_sub[y1:y2, x1:x2]

    plt.imshow(mask)
    plt.show()

    # Background Subtraction of 3 Regions [Y:Y, X:X]
    crop1 = (np.sum(dark_sub[3200:3600, 4400:4800]))/160000
    crop2 = (np.sum(dark_sub[200:600, 4000:4400])) /160000
    crop3 = (np.sum(dark_sub[3000:3400, 200:600]))/160000

    mean_crop = (crop1 + crop2 + crop3) * (abs((x1-x2)*(y1-y2)))/3

    # Sum of Star - Background
    sum_mask = np.sum(mask)
    back_sub = sum_mask - mean_crop

    # Radiance Calculation
    solid_angle = (abs((x1-x2)*(y1-y2))) * platescale_pixelsize * 2.35e-11
    radiance = back_sub / (qe * exp * solid_angle * pi * (r**2))
    
    # Values below calculated from '437A.py' script
    aldebaran_theory_780 = 1355415.3318381123
    aldebaran_theory_790 = 1368306.368678297
    aldebaran_theory_830 = 1409810.745338103
    aldebaran_theory_850 = 1424913.099174073

    # Calculating the Gamma factor
    gamma = aldebaran_theory_790/radiance

    print(gamma)


    ''' Calculating Background Radiance '''

    star_rad = 4.24E-06

    # Radiance Calculation of background
    radiance_back = star_rad * ((crop1 + crop2 + crop3) * 160000/3) / (qe * exp * solid_angle * pi * (r**2))
    
    print(radiance_back)

    ''''''''''''''''''''''''''''''''''''''''