import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np
import glob

path = r"C:\Users\veron\OneDrive\Desktop\Images_Paul\2020-02-26"
directories = glob.glob(f"{path}/*/*/*.xlsx")

hist_data = []
colors = []
hist_error = []

colordict = {
    '532nm': 'tomato',
    '780nm': 'k',
    '790nm': 'c',
    '830nm': 'g',
    '850nm': 'y'
    # '999nm': 'orchid'
}

for d in directories:

    # image = f'{d}.png'
    # name = f'{d}.Histogram.csv'
    
    csv_file = pd.read_excel(d, names = ['Channel', 'Lum'], encoding = 'utf-8')
    
    pixel = list(map(int, (csv_file.Channel.tolist())[5:260]))
    data = list(map(int, (csv_file.Lum.tolist())[5:260]))

    tmplabel = d.split('\\')[-3][-8:]

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

# ERROR CALCULATION
# for i in (np.array_split(hist_data, 6)):
#     hist_error.append(np.std(i))

################# AVERAGE ######################
# hist_avg = []

# for i in np.array_split(hist_data, 6):
#     for j in np.array_split(i, 18):
#         hist_avg.append(np.average(j))
        
# x_array = np.linspace(0, 1800, 18)

# colors_avg = ['tomato', 'k', 'c', 'g', 'y', 'orchid']

# legend = ['532nm', '780nm', '790nm', '830nm', '850nm', 'No Filter']

# fig, ax = plt.subplots()
# for i, j, k, l in zip(np.array_split(hist_avg, 6), colors_avg, legend, hist_error):
#     ax.scatter(x_array, i, color = j, s = 10, label = k)

# ax.set_xlabel('Time (seconds)')
# ax.set_ylabel('Sum of Dark Counts (1e6)')
# ax.set_title("Average Every 10 Points of Data")
# ax.legend()

# plt.show()
################################################

x_array = range(0,120)
legend = ['532nm', '780nm', '790nm', '830nm', '850nm']

fig, ax = plt.subplots()
print(len(hist_data))

for i, j, k in zip(np.array_split(hist_data, 5), np.array_split(colors, 5), legend ):
    ax.scatter(x_array, i, color = j, s = 10, label = k)
    # ax.errorbar(x_array, i, yerr = l, fmt = 'none', marker = 'none', zorder=0)

# IF ONLY PLOTTING SINGLE FILTER DATA
# ax.scatter(x_array, hist_data)

ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Sum of Dark Counts (1e6)')
ax.set_title("Data from Image")
ax.legend()

plt.show()
