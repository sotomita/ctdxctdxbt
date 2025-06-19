#! /usr/bin/env python3
# -*- conding: utf-8 -*-

import os
import sys
import pandas as pd

import namelist as nl

sys.path.append("../")
from xctd import get_xctd_df


os.makedirs(nl.output_dir, exist_ok=True)

# read field book
fbook_df = pd.read_csv(nl.field_book_path)

for i in range(len(fbook_df)):
    obskey = fbook_df["obskey"].iloc[i]
    filename = fbook_df["filename"].iloc[i]
    print(f"{obskey}:  {filename}")

    data_fpath = f"{nl.input_dir}/{filename}"
    # read data file path
    df = get_xctd_df(data_fpath)

    # save data as csv.
    df.to_csv(f"{nl.output_dir}/{obskey}.csv")
