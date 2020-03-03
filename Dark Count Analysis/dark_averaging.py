import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np
import glob

path = r"C:\Users_eron\OneDrive\Desktop\02-28-2020_NoFilter_Fan"
directories = glob.glob(f"{path}/*/*.csv")

hist_data = []
colors = []
# hist_error = []

colordict = {
    '532': 'tomato',
    '780': 'k',
    '790': 'c',
    '830': 'g',
    '850': 'y'
    # '999nm': 'orchid'
}

for d in directories:

    # image = f'{d}.png'
    # name = f'{d}.Histogram.csv'
    
    csv_file = pd.read_csv(d, names = ['Channel', 'Lum'])
    pixel = list(map(int, (csv_file.Channel.tolist())[5:260]))
    data = list(map(int, (csv_file.Lum.tolist())[5:260]))

    # tmplabel = d.split('\\')[-2][-7:]

    # if not tmplabel[0].isdigit():
    #     tmplabel = tmplabel[1:]
    # color = colordict[tmplabel.split('_')[0]]

    # colors.append(color)

    tmp = np.array(pixel) * np.array(data)
    hist_data.append(np.sum(tmp))
    ########### TRIMMING ###################
    # im = Image.open(image)
    # width, height = im.size 
    # image1 = np.array(im.crop((150, 150, width - 150 , height - 150)))
    # hist_data.append((image1.sum())/1e6)
    # tmplabel = image.split('\\')[-3][-10:]
    ########################################

# ERROR CALCULATION
# for i in (np.array_split(hist_data, 6)):
#     hist_error.append(np.std(i))

# x_array = range(0, 120)

############ TO AVERAGE ################
x_array = range(0, 24)

temp = np.array_split(hist_data, 5) 

hist_data = []
for i in temp:
    tmp = np.array_split(i, 24)
    for j in tmp:
        hist_data.append(np.average(j))

legend = ['532nm', '780nm', '790nm', '830nm', '850nm']

fig, ax = plt.subplots()

colors = ['tomato', 'k', 'c', 'g', 'y']
#########################################

# for i, j, k in zip(np.array_split(hist_data, 5), colors, legend ):
    
#     ax.scatter(x_array, i, color = j, s = 10, label = k)
    # ax.errorbar(x_array, i, yerr = l, fmt = 'none', marker = 'none', zorder=0)

# IF ONLY PLOTTING SINGLE FILTER DATA
# print(len(hist_data))
tmp = np.array_split(hist_data, 24)
hist_data = [np.average(i) for i in tmp]
ax.scatter(x_array, hist_data)

ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Sum of Dark Counts')
ax.set_title("Data from Images- No Filter_With Fan")
ax.set_ylim(4e7, 5e7)
ax.legend()

plt.show()
