* `mkdir -p ./csvs/`
* Generate CSV
```sh
python preprocess_generate_csv.py --csv=csvs/msrvtt.csv --video_root_path /var/scratch/pbagad/datasets/MSR-VTT/MSRVTT/videos/all/ --feature_root_path /var/scratch/pbagad/datasets/MSR-VTT/MSRVTT/feat/feat_how2_s3d_dim1024/ 
```


### DiDeMo

```sh
vdir=/var/scratch/pbagad/datasets/DiDeMo/videos/
fdir=/var/scratch/pbagad/datasets/DiDeMo/feat/feat_how2_s3d_dim1024/

# generate csv
python preprocess_generate_csv.py --csv=csvs/didemo.csv --video_root_path $vdir --feature_root_path $fdir

# activate the environment
conda activate videoclip
cd /var/scratch/pbagad/projects/VideoFeatureExtractor/

# generate features
python extract.py --csv=./csvs/didemo.csv --type=s3dg --batch_size=64 --num_decoding_thread=4
```

### Charades

```sh
vdir=/var/scratch/pbagad/datasets/Charades/Charades_v1_480/
fdir=/var/scratch/pbagad/datasets/Charades/feat/feat_how2_s3d_dim1024/

python preprocess_generate_csv.py --csv=csvs/charades.csv --video_root_path $vdir --feature_root_path $fdir
python extract.py --csv=./csvs/charades.csv --type=s3dg --batch_size=64 --num_decoding_thread=4
```

### ActivityNet

```sh
vdir=/var/scratch/pbagad/datasets/activitynet-1.3/VideoData/
fdir=/var/scratch/pbagad/datasets/activitynet-1.3/feat/feat_how2_s3d_dim1024/
python preprocess_generate_csv.py --csv=csvs/activitynet.csv --video_root_path $vdir --feature_root_path $fdir
python extract.py --csv=./csvs/activitynet.csv --type=s3dg --batch_size=64 --num_decoding_thread=4
```

### YouCook2

```sh
# see youcook2_generate_csv.py to generate CSV and then run rest of the commands
```

### SSv2

### NextQA

### AGQA