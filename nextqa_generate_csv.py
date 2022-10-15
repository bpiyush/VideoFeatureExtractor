"""Generates CSV for YouCook2"""
from genericpath import exists
import os
from os.path import join
from glob import glob
from tqdm import tqdm
import pandas as pd

splits = ["validation", "test"]

df = {"video_path": [], "feature_path": []}

vdir = f"/var/scratch/pbagad/datasets/next-qa/video/"
vfolders = glob(join(vdir, "*"))

fdir = f"/var/scratch/pbagad/datasets/next-qa/feat/feat_how2_s3d_dim1024/"
os.makedirs(fdir, exist_ok=True)

for vf in tqdm(vfolders, desc="Generating CSV"):
    vfiles = glob(join(vf, "*.mp4"))
    for vf in vfiles:
        df["video_path"].append(vf)
        ff = vf.replace(".mp4", ".npy").replace(vdir, fdir)
        df["feature_path"].append(ff)
df = pd.DataFrame(df)
df = df[df["video_path"].apply(exists)]
df.to_csv("./csvs/next-qa_v1.csv")
print("Saved csv file to ./csvs/next-qa_v1.csv")