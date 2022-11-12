import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# grab the data
board01 = pd.read_csv('board01/DB2.1_#01board_combined.csv')
board03 = pd.read_csv('board03/combined.csv')

df = pd.concat([board01, board03])
print(df)

# multi graph chart
fig, ax = plt.subplots(1,2, figsize=(30,10))

#plot the line of average intesity at given wavelength for a given polymer type
polys = len(df['Type'].unique())
import matplotlib.cm as cm
color_num = 0
colors = cm.get_cmap('jet', polys)

for poly in df['Type'].unique():
    # subset data
    poly_df = df[df['Type'] == poly]
    # take only wavelength data
    poly_df = poly_df[['940','1050','1200','1300','1450','1550','1650','1720']]
    # get mean and standard deviation of values
    mean_intensity = poly_df.mean().values
    std_intensity = poly_df.std().values
    ynerror = np.subtract(mean_intensity, std_intensity)
    yperror = np.add(mean_intensity, std_intensity)
    # get wavelengths as array 
    wavelengths = list(map(int,poly_df.columns.tolist()))
    ax[0].plot(wavelengths, poly_df.mean().values, color=colors(color_num), label=poly)
    ax[0].fill_between(wavelengths, ynerror, yperror, alpha=0.5, facecolor=colors(color_num))
    color_num += 1


# finish plotting our results
ax[0].set_xlabel('wavelength (nm)', fontsize=20)
ax[0].set_ylabel('intensity (a.u.)', fontsize=20)
ax[0].title.set_text('By Polymer')
ax[0].legend()


#plot the line of average intesity at given wavelength for a given polymer colorant
colors = len(df['Color'].unique())
import matplotlib.cm as cm
color_num = 0
colors = cm.get_cmap('jet', colors)

# drop the values where we don't know the color
df = df.dropna(subset=['Color'])

print(df['Color'].unique())
color_dict = {'white':'silver','purple':'purple','transparent':'lightblue','blue':'blue','red transparent':'darkred','green':'green','yellow':'yellow','pink':'pink','red':'red','white transparent':'grey','gold':'gold','grey':'grey','white black white':'dimgray','brown':'brown','black':'black','orange':'orange'}
for color in df['Color'].unique():
    # subset data
    poly_df = df[df['Color'] == color]
    # take only wavelength data
    poly_df = poly_df[['940','1050','1200','1300','1450','1550','1650','1720']]
    # get mean and standard deviation of values
    mean_intensity = poly_df.mean().values
    std_intensity = poly_df.std().values
    ynerror = np.subtract(mean_intensity, std_intensity)
    print(ynerror)
    yperror = np.add(mean_intensity, std_intensity)
    # get wavelengths as array 
    wavelengths = list(map(int,poly_df.columns.tolist()))

    # plot
    ax[1].plot(wavelengths, poly_df.mean().values, color=color_dict[color], label=color)
    ax[1].fill_between(wavelengths, ynerror, yperror, alpha=0.5, facecolor=color_dict[color])
    color_num += 1


# finish plotting our results
ax[1].set_xlabel('wavelength (nm)', fontsize=20)
ax[1].set_ylabel('intensity (a.u.)', fontsize=20)
ax[1].title.set_text('By Colorant')
ax[1].legend()

plt.show()
