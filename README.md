# HeadSwap

## LeslieZhoa-Head-Swap

Tested on 11.7 cuda

1. git clone https://github.com/yachty66/LeslieZhoa-Head-Swap.git

2. cd HeadSwap

3. pip install -r requirements.txt

4. python downloader.py

5. python inference.py

## Facefusion

apt-get update

apt-get install git

apt install git-all

apt install curl

curl -LO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh

apt install ffmpeg

~/miniconda3/bin/conda install conda-forge::cuda-runtime=12.6.3 conda-forge::cudnn=9.3.0.75

~/miniconda3/bin/conda init --all

~/miniconda3/bin/conda create --name facefusion python=3.12

conda activate facefusion

git clone https://github.com/facefusion/facefusion

cd facefusion

python install.py --onnxruntime cuda

conda deactivate

conda activate facefusion

mkdir output

python facefusion.py headless-run \
    --keep-temp \
    --log-level warn \
    --execution-providers cuda \
    --execution-thread-count 16 \
    --execution-queue-count 2 \
    --temp-frame-format png \
    --face-selector-mode many \
    --face-mask-types box occlusion \
    --processors face_swapper face_enhancer \
    --face-enhancer-model gfpgan_1.4 \
    --face-enhancer-blend 80 \
    --face-swapper-model inswapper_128 \
    --face-detector-model retinaface \
    -s source.jpg \
    -t target.jpg \
    -o ./output/result.jpg


    s