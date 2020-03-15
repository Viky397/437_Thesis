import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np
import glob

path = r"C:\Users_eron\FAN ON"
directories = glob.glob(f"{path}/*/*/")

hist_data = []
colors = []

colordict = {
    '532nm': 'tomato',
    '780nm': 'k',
    '790nm': 'c',
    '830nm': 'g',
    '850nm': 'y'
    # '999nm': 'orchid'
}

for name in directories:

    # image = f'{name}.png'
    name = f'{name}.png.Histogram.csv'
    
    csv_file = pd.read_csv(name, names = ['Channel', 'Lum'])
    pixel = list(map(int, (csv_file.Channel.tolist())[5:260]))
    data = list(map(int, (csv_file.Lum.tolist())[5:260]))

    tmplabel = name.split('\\')[-3][-8:]

    if not tmplabel[0].isdigit():
        tmplabel = tmplabel[1:]
    color = colordict[tmplabel.split('_')[0]]
    colors.append(color)

    tmp = np.array(pixel) * np.array(data)
    hist_data.append(np.sum(tmp))
    ########### TRIMMING ###################
    # im = Image.open(image)
    # width, height = im.size 
    # image1 = np.array(im.crop((150, 150, width - 150 , height - 150)))
    # hist_data.append((image1.sum())/1e6)
    # tmplabel = image.split('\\')[-3][-10:]
    ########################################

############ TO AVERAGE ################
# x_array = range(0, 24)

# temp = np.array_split(hist_data, 5) 

# hist_data = []
# for i in temp:
#     tmp = np.array_split(i, 24)
#     for j in tmp:
#         hist_data.append(np.average(j))

# colors = ['tomato', 'k', 'c', 'g', 'y']
#########################################

x_array = range(0, 120)
legend = ['532nm', '780nm', '790nm', '830nm', '850nm']
fig, ax = plt.subplots()

for i, j, k in zip(np.array_split(hist_data, 5), np.array_split(colors,5), legend):
    
    ax.scatter(x_array, i, color = j, s = 10, label = k)

# IF ONLY PLOTTING SINGLE FILTER DATA
# print(len(hist_data))
# tmp = np.array_split(hist_data, 24)
# hist_data = [np.average(i) for i in tmp]
# ax.scatter(x_array, hist_data)

ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Sum of Dark Counts')
ax.set_title("Dark Counts Over Time: Fan On, Filter Wheel Detached")
# ax.set_ylim(4e7, 5e7)
ax.legend()

plt.show()
