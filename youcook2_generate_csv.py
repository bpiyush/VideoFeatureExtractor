"""Generates CSV for YouCook2"""
from genericpath import exists
import os
from os.path import join
from glob import glob
from tqdm import tqdm
import pandas as pd

splits = ["validation", "test"]

df = {"video_path": [], "feature_path": []}
for split in splits:
    split = "validation"
    vdir = f"/var/scratch/pbagad/datasets/youcook2/raw_videos/{split}"
    vfolders = glob(join(vdir, "*"))

    fdir = f"/var/scratch/pbagad/datasets/youcook2/feat/feat_how2_s3d_dim1024/{split}"
    os.makedirs(fdir, exist_ok=True)

    for vf in tqdm(vfolders, desc="Generating CSV"):
        vfiles = glob(join(vf, "*.mp4"))
        for vf in vfiles:
            df["video_path"].append(vf)
            ff = vf.replace(".mp4", ".npy").replace(vdir, fdir)
            df["feature_path"].append(ff)
df = pd.DataFrame(df)
df = df[df["video_path"].apply(exists)]
df.to_csv("./csvs/youcook2_v1.csv")
print("Saved csv file to ./csvs/youcook2_v1.csv")