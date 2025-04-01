from huggingface_hub import snapshot_download
while True:
    try:
        snapshot_download(repo_id="kelvin34501/OakInk-v2", repo_type="dataset", local_dir="./OakInk-v2-hub", cache_dir="./hub", local_dir_use_symlinks=True)
    except Exception:
        print("restart")
    break
