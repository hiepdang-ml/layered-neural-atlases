conda create --name neural_atlases python=3.7 
conda activate neural_atlases 

conda install pytorch=1.6.0 -c pytorch
conda install torchvision=0.7.0 -c pytorch
conda install cudatoolkit=10.1 -c pytorch

pip install matplotlib
pip install tensorboard
pip install scipy
pip install scikit-image
pip install tqdm
pip install imageio-ffmpeg gdown
pip install opencv-python
pip install detectron2 -f   https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.6/index.html

