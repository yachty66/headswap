from huggingface_hub import snapshot_download
import os

def download_pretrained_models():
    # Define the repo ID
    repo_id = "yachty66/LeslieZhoa-Head-Swap"
    
    try:
        # Download only the pretrained_models folder
        snapshot_download(
            repo_id=repo_id,
            allow_patterns="pretrained_models/*",  # Only download files in pretrained_models
            local_dir=".",  # Download to current directory
            local_dir_use_symlinks=False  # Get actual files, not symlinks
        )
        print("Successfully downloaded pretrained_models folder")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_pretrained_models()