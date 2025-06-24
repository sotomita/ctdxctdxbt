#!/usr/bin/env python3

import os, sys
from glob import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["font.size"] = 14
import matplotlib.dates as mdates
import namelist

fpath = namelist.field_book_path
qc_data_dir = namelist.output_dir

# output fig dir
fig_dir = "./fig/time_seq"

# available variables
#'depth', 'Temp', 'Conductivity', 'Salinity', 'Sound Velocity',
#       'Density'

var = "Temp"

# bottom pressure of figure
bottom = 1000.0  # m

# cut data to remove noise, must be integer
cut_top = 2  # m
cut_bottom = 50  # m

# range of times
times = pd.date_range("2022-06-19 06", "2022-06-20 21", freq="h")

######################### no need to edit below

os.makedirs(fig_dir, exist_ok=True)
fig_path = f"{fig_dir}/{var}.png"

# range of depth level
z = np.arange(0.0, bottom, 1.0)


def draw_time_seq(x, p, ar):

    ax = plt.axes()
    # shade=ax.contourf(times,p,ar)#,np.arange(290,320,1))
    shade = ax.pcolormesh(times, p, ar)  # ,np.arange(290,320,1))
    plt.colorbar(shade)

    ax.set_ylim([bottom, 0.0])

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%H"))
    plt.xticks(rotation=45)

    ax.set_title(var)

    plt.tight_layout()
    plt.savefig(fig_path, dpi=512)


def calc_pot(t, p):
    k = 2 / 7
    return t * ((1000 / p) ** k)


def check_time(launch_time):

    launch_time_pd = launch_time  # + pd.Timedelta(minutes=30)
    nearest_00_time = launch_time_pd.round("h")
    for i, t in enumerate(times):
        if t == nearest_00_time:
            return i
    print("no matched time, change range of times")
    exit()


def main():

    csvs = glob(f"{qc_data_dir}/*csv")

    N = len(times)
    x = np.arange(N)
    ar = np.full((len(z), N), np.nan)

    for j, file_name in enumerate(csvs):
        print("read ", file_name)

        df = pd.read_csv(file_name, index_col=0)

        _time = file_name.split("_")[1]
        y = _time[0:4]
        m = _time[4:6]
        d = _time[6:8]
        h = _time[8:10]
        s = _time[10:12]
        launch_time = pd.to_datetime(f"{y}-{m}-{d} {h}:{s}:00")

        idx_t = check_time(launch_time)

        Z = df["depth"].values[cut_top:-cut_bottom]

        A = df[var].values[cut_top:-cut_bottom]

        # idx_z = [True if _z in Z else False for _z in z]
        Z_min = np.nanmin(Z)
        Z_max = np.nanmax(Z)
        # print(P_max,P_min)
        idx_0 = 0
        idx_1 = len(z)
        inner = False
        for i, _z in enumerate(z):
            if _z == Z_min:
                idx_0 = i
            if _z == Z_max:
                inner = True
                idx_1 = i + 1
                break

        if not inner:
            A = A[: idx_1 - idx_0]

        ar[idx_0:idx_1, idx_t] = A

    # unwanted columns
    # ar[:,5] = np.nan
    # ar[:,8] = np.nan

    draw_time_seq(x, z, ar)
    print("done.")


main()
