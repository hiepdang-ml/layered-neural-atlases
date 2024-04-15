python -m venv .neural_atlases

source .neural_atlases/bin/activate

pip install matplotlib
pip install tensorboard
pip install scipy
pip install scikit-image
pip install tqdm
pip install imageio-ffmpeg gdown
pip install opencv-python

python -m pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113
git clone https://github.com/facebookresearch/detectron2.git
pip install -e detectron2
