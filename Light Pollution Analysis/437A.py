from __future__ import division
import numpy as np
import scipy.integrate as integ
import astropy.constants as const
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pysynphot as S
import astropy
from astropy.modeling import models, fitting
from astropy.io import fits
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import warnings

# h = 6.63E-34
# c = 3.00E8
# k = 1.38E-23

# '''
# My coding of BB function
# '''
# # def black_body(lam,T):

# #     num = (2*h*c**2)/((lam)**5)
# #     denom = (np.exp((h*c)/(lam*T*k))-1)
# #     return(num/denom)

# # x = np.arange(512, 552, 0.5)
# # y = np.array(black_body(x*1E-9, 9602))

# # y_func = integ.simps(y, x)

# # photon_flux = (y_func*0.55/(h*c/(532*1E-9)))
# # print('Number of photons:', photon_flux)

# # plt.plot(x, y)
# # plt.ylabel('$B_{\lambda}$')
# # plt.xlabel('$\lambda$')

# # plt.show()
# '------------------------------------------------------------'

# '''
# Built-in coding of BB- Vega
# '''

# wave = np.arange(5120, 5520, 0.04)
# # wave = np.arange(0, 30000)

# bb = S.BlackBody(9602)
# flux_real = []

# for i in wave:
#     flux_real.append(bb.sample(i))

# y_func = integ.simps(flux_real, wave)
# photon_flux = (y_func*0.55*1E-10/(h*c/(532*1E-9)))

# print('Number of photons:', photon_flux)

# plt.plot(wave, flux_real)

# # plt.xlabel(r'$Wavelength (\AA)$')
# # plt.ylabel('$B_{\lambda}$')
# # plt.title('Blackbody Spectrum of Vega (T = 9602 K)')
# # plt.show()

# '------------------------------------------------------------'

# # '''
# # Plotting middle row and column of the region
# # Buffer_Points
# # '''
# # image = mpimg.imread('Vega_frame1.tif')
# # # print(image)
# # imarray = np.array(image, dtype = float)
# # # ind = np.unravel_index(np.argmax(imarray, axis = None), imarray.shape)
# # # print(imarray)
# # def points_in_circle(circle, arr):
# #     buffer_points = []
# #     i0, j0, r = circle

# #     def int_ceiling(x):
# #         return int(np.ceil(x))

# #     for i in range(int_ceiling(i0 - r), int_ceiling(i0 + r)):
# #         ri = np.sqrt(r**2 - (i - i0)**2)

# #         for j in range(int_ceiling(j0 - ri), int_ceiling(j0 + ri)):
# #             buffer_points.append(arr[i][j])
            
# #     return buffer_points

# # circle = (887, 361, 7.8325485)
# # buffer_points = points_in_circle(circle, imarray)

# # mean = np.mean(buffer_points)

# # row = imarray[887 - 8: 887 + 8, 361]
# # column = imarray[887, 361 - 8: 361 + 8]

# # # plt.plot(range(879, 895), row, label = 'row')
# # # plt.plot(range(879, 895), column, label = 'column')
# # # plt.legend(loc=2)
# # # plt.show()

# # '------------------------------------------------------------'
# '''
# Canned Function- Gaussian model fitting
# '''

# # Load the data and find center of PSF
# cents = np.where(image == np.max(image))
# print(cents)
# xc = int(cents[1])
# yc = int(cents[0])

# # Cut out smaller box around PSF
# bb = 10
# box = image[yc-bb:yc+bb,xc-bb:xc+bb]
# yp, xp = box.shape

# # print(box)
# # Generate grid of same size like box to put the fit on
# y, x, = np.mgrid[:yp, :xp]
# # Declare what function you want to fit to your data
# f_init = models.Gaussian2D()
# # Declare what fitting function you want to use
# fit_f = fitting.LevMarLSQFitter()

# # Fit the model to your data (box)
# f = fit_f(f_init, x, y, box)

# # Plot the data with the best-fit model
# # plt.figure(figsize=(8, 2.5))
# # plt.subplot(1, 3, 1)
# # plt.imshow(box)
# # plt.title("Data")
# # plt.subplot(1, 3, 2)
# # plt.imshow(f(x, y))
# # plt.title("Model")
# # plt.subplot(1, 3, 3)
# # plt.imshow(box - f(x, y))
# # plt.title("Residual")
# # plt.show()
# # '------------------------------------------------------------'
# # 1D Curve Fit

# # Fit the data using a Gaussian
# g_init = models.Gaussian1D(amplitude=33., mean=887, stddev=10.)
# fit_g = fitting.LevMarLSQFitter()

# x = [879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894]
# y = [ 1,  1,  2,  1,  2,  3,  5, 10, 33, 17,  7,  3,  2,  1,  2,  1]

# g = fit_g(g_init, x, y)

# max_y = max(y)  # Find the maximum y value
# xs = [x for x in range(16) if y[x] > max_y/2.0]
# # print(min(xs), max(xs)) # Print the points at half-maximum

# # # Plot the data with the best-fit model
# # plt.plot(x, y, 'ko')
# # plt.plot(x, g(x), label='Gaussian')
# # plt.xlabel('Position')
# # plt.ylabel('Flux')
# # plt.legend(loc=2)
# # plt.show()

'------------------------------------------------------------'
# Point spread function!

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

x = np.arange(1240)
y = np.arange(1028)

I = np.zeros((x.size, y.size))

for i in x:
    for j in y:
        I[i][j] = (33*(np.exp((-(i-362)**2)/0.36))*(np.exp((-(j-887)**2)/0.36)))

plt.figure()
plt.contour(I, 30)
plt.colorbar()
plt.title('2D Point Spread Function')
plt.xlabel('Distance in Pixels (x-axis)')
plt.ylabel('Distance in Pixels (y-axis)')
plt.ylim(361, 363)
plt.xlim(886,888)
plt.show()

X,Y = np.meshgrid(y,x)
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,I,30)
plt.ylim(361, 363)
plt.xlim(886,888)
plt.show()



