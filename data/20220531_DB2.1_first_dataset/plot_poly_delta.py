import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# grab the data
board01 = pd.read_csv('board01/DB2.1_#01board_combined.csv')
board03 = pd.read_csv('board03/combined.csv')

df = pd.concat([board01, board03])

# multi graph chart
fig, ax = plt.subplots(1,3, figsize=(40,10))

#plot line of intesity at given wavelength for each polymer colored by type
polys = len(df['Type'].unique())
import matplotlib.cm as cm
color_num = 0
colors = cm.get_cmap('jet', polys)

for poly in df['Type'].unique():
    # subset data
    poly_df = df[df['Type'] == poly]
    poly_df = poly_df[['940','1050','1200','1300','1450','1550','1650','1720']]
    # get wavelengths as array 
    wavelengths = list(map(int,poly_df.columns.tolist()))
    for index, row in poly_df.iterrows():
        print(row)
        # take only wavelength data
        intensity = row.values
        ax[0].plot(wavelengths, intensity, color=colors(color_num), label='_nolegend_')
    color_num += 1


# finish plotting our results
ax[0].set_xlabel('wavelength (nm)', fontsize=20)
ax[0].set_ylabel('intensity (a.u.)', fontsize=20)
ax[0].title.set_text('By Individual')
ax[0].legend()

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
    ax[1].plot(wavelengths, poly_df.mean().values, color=colors(color_num), label=poly)
    ax[1].fill_between(wavelengths, ynerror, yperror, alpha=0.5, facecolor=colors(color_num))
    color_num += 1


# finish plotting our results
ax[1].set_xlabel('wavelength (nm)', fontsize=20)
ax[1].set_ylabel('intensity (a.u.)', fontsize=20)
ax[1].title.set_text('By Polymer')
ax[1].legend()

#plot the line of average intesity at given wavelength for a given polymer type
polys = len(df['Type'].unique())
import matplotlib.cm as cm
color_num = 0
colors = cm.get_cmap('jet', polys)

# create a baseline for the intensity
baseline = df[['940','1050','1200','1300','1450','1550','1650','1720']].mean().values

for poly in df['Type'].unique():
    # subset data
    poly_df = df[df['Type'] == poly]
    # take only wavelength data
    poly_df = poly_df[['940','1050','1200','1300','1450','1550','1650','1720']]
    # subtract baseline 
    print(poly_df)
    poly_df = poly_df.sub(baseline)
    print(poly_df)
    # get mean and standard deviation of values
    mean_intensity = poly_df.mean().values
    std_intensity = poly_df.std().values
    ynerror = np.subtract(mean_intensity, std_intensity)
    yperror = np.add(mean_intensity, std_intensity)
    # get wavelengths as array 
    wavelengths = list(map(int,poly_df.columns.tolist()))
    ax[2].plot(wavelengths, poly_df.mean().values, color=colors(color_num), label=poly)
    ax[2].fill_between(wavelengths, ynerror, yperror, alpha=0.5, facecolor=colors(color_num))
    color_num += 1


# finish plotting our results
ax[2].set_xlabel('wavelength (nm)', fontsize=20)
ax[2].set_ylabel('intensity delta (a.u.)', fontsize=20)
ax[2].title.set_text('Intensity Delta')
ax[2].legend()

plt.savefig('sensor_data.png')

