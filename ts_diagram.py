#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import gsw

import namelist as nl


# --- fig settings
# salinity
min_sp = 33  # psu
max_sp = 35  # psu
sp_ticks = np.arange(33, 35.1, 0.5)

# temperature
min_tmp = -2  # degC
max_tmp = 30  # degC
tmp_ticks = np.arange(0, 31, 5)

# ref point
lat = 35  # deg
lon = 140  # deg
p = 0  # dbar

fig_dir = f"{nl.fig_dir}/tsdiagram"
os.makedirs(fig_dir, exist_ok=True)


# ===== DO NOT EDIT BELOW =====

# --- calculate  the sigma
sp_den_diff = 0.1
tmp_den_diff = 1
sp = np.arange(min_sp, max_sp + sp_den_diff, sp_den_diff)
tmp = np.arange(min_tmp, max_tmp + tmp_den_diff, tmp_den_diff)
sp_mesh, tmp_mesh = np.meshgrid(sp, tmp)
sa = gsw.SA_from_SP(sp_mesh, p, lon=lon, lat=lat)
ct = gsw.CT_from_t(sa, tmp_mesh, p)
rho = gsw.rho(sa, ct, p)
sigma = rho - 1000


def plot_tsdiagram(
    sp: np.ndarray,
    tmp: np.ndarray,
    fig_path: str,
    min_sp: float = 33,
    max_sp: float = 35,
    sp_ticks: np.ndarray = np.arange(33, 35.1, 0.5),
    min_tmp: float = -2,
    max_tmp: float = 30,
    tmp_ticks: np.ndarray = np.arange(0, 31, 5),
) -> None:
    """plot T-S diagram"""

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(f"{obskey}")

    # x axis
    ax.set_xlabel("Salinity[psu]")
    ax.set_xlim(min_sp, max_sp)
    ax.set_xticks(sp_ticks)

    # yaxis
    ax.set_ylabel("Temperature [degC]")
    ax.set_ylim(min_tmp, max_tmp)
    ax.set_yticks(tmp_ticks)

    # sigma contour
    ax.contour(
        sp_mesh,
        tmp_mesh,
        sigma,
        levels=np.arange(0, 50, 0.2),
        colors="gray",
        linewidths=0.7,
    )
    c = ax.contour(
        sp_mesh,
        tmp_mesh,
        sigma,
        levels=np.arange(0, 50, 1),
        colors="k",
        linewidths=1,
    )
    plt.clabel(c, fmt=r"%.1f$\sigma$", fontsize=8)

    # plot t-s curve
    ax.scatter(sp, tmp, c="k", s=0.5)

    plt.savefig(fig_path, dpi=512)
    plt.close()


# read field book
fbook_df = pd.read_csv(nl.field_book_path)

for i in range(len(fbook_df)):
    obskey = fbook_df["obskey"].iloc[i]
    print(obskey)

    fpath = glob(f"{nl.output_dir}/{obskey}*.csv")[0]
    df = pd.read_csv(fpath, index_col=0)

    sp = df["Salinity"].to_numpy()
    tmp = df["Temp"].to_numpy()
    fig_path = f"{fig_dir}/{obskey}_{p}.png"

    plot_tsdiagram(
        sp,
        tmp,
        fig_path,
        min_sp,
        max_sp,
        sp_ticks,
        min_tmp,
        max_tmp,
        tmp_ticks,
    )
