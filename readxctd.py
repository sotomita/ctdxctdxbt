#! /usr/bin/env python3
# -*- conding: utf-8 -*-

import os
import sys

sys.path.append("../")
from xctd import get_xctd_df


data_fpath = (
    "/home/aoi/research/ctdxctdxbt/data/XCTD/rawdata/XCTD-0S1120220617_all.CTD"
)
st_name = "test"
save_dir = "/home/aoi/research/ctdxctdxbt/data/XCTD/anl"


os.makedirs(save_dir, exist_ok=True)

df = get_xctd_df(data_fpath)
df.to_csv(f"{save_dir}/{st_name}.csv")
