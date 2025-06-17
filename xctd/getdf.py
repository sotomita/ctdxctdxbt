#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


def get_float(x) -> float:
    return float(x)


def get_xctd_df(fpath: str) -> pd.DataFrame:
    dpth_list = []
    tmp_list = []
    cnd_list = []
    sal_list = []
    sve_list = []
    den_list = []
    with open(fpath, "r") as file:

        # read a header record
        header = file.read(256)

        # read data records
        data = file.read().split("\n")[:-1]

        num_records = len(data)

        for i in range(num_records):

            d = data[i].split(",")
            if len(d) != 7:
                break
            dpth = get_float(d[0])
            tmp = get_float(d[1])
            cnd = get_float(d[2])
            sal = get_float(d[3])
            sve = get_float(d[4])
            den = get_float(d[5])

            dpth_list.append(dpth)
            tmp_list.append(tmp)
            cnd_list.append(cnd)
            sal_list.append(sal)
            sve_list.append(sve)
            den_list.append(den)

    df = pd.DataFrame(
        {
            "depth": dpth_list,
            "Temp": tmp_list,
            "Conductivity": cnd_list,
            "Salinity": sal_list,
            "Sound Velocity": sve_list,
            "Density": den_list,
        }
    )

    return df
