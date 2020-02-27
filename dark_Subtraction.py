import numpy as np
from PIL import Image

dark1 = Image.open('dark1.tif')
dark2 = Image.open('dark2.tif')

vega1 = Image.open('Vega_frame1.tif')
vega2 = Image.open('Vega_frame2.tif')
deneb1 = Image.open('Deneb_frame1.tif')
deneb2 = Image.open('Deneb_frame2.tif')
altair1 = Image.open('Altair_frame1.tif')
altair2 = Image.open('Altair_frame2.tif')

'----------------------------------------------------'

dark_array1 = np.array(dark1)[:,:,3]
dark_array2 = np.array(dark2)[:,:,0] + np.array(dark1)[:,:,3]
print(dark_array1)
vega_array1 = np.array(vega1)
vega_array2 = np.array(vega2)
deneb_array1 = np.array(deneb1)
deneb_array2 = np.array(deneb2)
altair_array1 = np.array(altair1)
altair_array2 = np.array(altair2)

# dark_1= dark_array1[:,:,1]
# dark_2 = dark_array1[:,:,2]
# print(dark_1-dark_2)

vega1_subtracted = vega_array1 - dark_array1
# vega1_subtracted[vega1_subtracted < 0] == 0
# vega1_subtracted = np.mean(vega1_subtracted)

deneb1_subtracted = deneb_array1 - dark_array1
deneb2_subtracted = deneb_array2 - dark_array2
altair1_subtracted = altair_array1 - dark_array1
altair2_subtracted = altair_array2 - dark_array2

vega_image1 = Image.fromarray(vega1_subtracted)
vega_image1.show()
vega_image1.save("VEGA.tif")
