conda install pytorch torchvision -c pytorch
pip install mmcv-full
cd mmdetection
pip install -r requirements/build.txt
pip install -v -e .  
cd ..
cd ./cocoapi/PythonAPI
python setup.py install
