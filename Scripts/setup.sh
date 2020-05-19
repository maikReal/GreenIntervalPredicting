echo "Install tensorfllow API..."
pip install tensorflow-object-detection-api

echo "Install dependencies in Tesnorflow API..."
python ../models/research/setup.py build
python ../models/research/setup.py install
python ../models/research/slim/setup.py build
python ../models/research/slim/setup.py install

echo "Install Tensorflow 1.15..."
pip install tensorflow==1.15

mkdir TmpDetectionResults