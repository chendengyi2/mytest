import os

# 定义需创建的目标目录列表，避免路径不存在导致下载失败
target_dirs = [
    "nsddata/experiments/nsd/",
    "nsddata_stimuli/stimuli/nsd/",
    # 为每个受试者和会话创建beta数据目录
    *[f"nsddata_betas/ppdata/subj{sub:02d}/func1pt8mm/betas_fithrf_GLMdenoise_RR/" for sub in [1,2,5,7]],
    # 为每个受试者创建ROI目录
    *[f"nsddata/ppdata/subj{sub:02d}/func1pt8mm/roi/" for sub in [1,2,5,7]]
]

# 循环创建目录（递归创建父目录，已存在则忽略）
for dir_path in target_dirs:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        print(f"已创建目录：{dir_path}")

# Download Experiment Infos（添加--no-sign-request跳过凭证验证）
os.system('aws s3 cp --no-sign-request s3://natural-scenes-dataset/nsddata/experiments/nsd/nsd_expdesign.mat nsddata/experiments/nsd/')
os.system('aws s3 cp --no-sign-request s3://natural-scenes-dataset/nsddata/experiments/nsd/nsd_stim_info_merged.pkl nsddata/experiments/nsd/')

# Download Stimuli（添加--no-sign-request跳过凭证验证）
os.system('aws s3 cp --no-sign-request s3://natural-scenes-dataset/nsddata_stimuli/stimuli/nsd/nsd_stimuli.hdf5 nsddata_stimuli/stimuli/nsd/')

# Download Betas（添加--no-sign-request跳过凭证验证）
for sub in [1,2,5,7]:
    for sess in range(1,38):
        os.system('aws s3 cp --no-sign-request s3://natural-scenes-dataset/nsddata_betas/ppdata/subj{:02d}/func1pt8mm/betas_fithrf_GLMdenoise_RR/betas_session{:02d}.nii.gz nsddata_betas/ppdata/subj{:02d}/func1pt8mm/betas_fithrf_GLMdenoise_RR/'.format(sub,sess,sub))

# Download ROIs（添加--no-sign-request跳过凭证验证）
for sub in [1,2,5,7]:
    os.system('aws s3 cp --no-sign-request s3://natural-scenes-dataset/nsddata/ppdata/subj{:02d}/func1pt8mm/roi/* nsddata/ppdata/subj{:02d}/func1pt8mm/roi/'.format(sub,sub))

print("所有数据下载命令已执行完毕，可检查目标目录确认下载结果。")
