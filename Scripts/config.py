import os
import numpy as np

# ROOT OF THE PROJECT
project_path = os.path.join('../')

# PATH TO IMAGES
data_path = os.path.join(project_path, 'Data')
images = os.path.join(data_path, 'Images')

# PATH TO MODEL
model_path = os.path.join(project_path, 'Inference_graph')

# PATH TO TRAINING FOLDER
training_path = os.path.join(project_path, 'Training')

# Path to frozen detection graph. 
PATH_TO_FROZEN_GRAPH = 'Inference_graph/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = 'Data/label_map.pbtxt'

#Number of classes
NUM_CLASSES = 3

# Path to folder with test images 
# PATH_TO_TEST_IMAGES_DIR = 'Data/Test'
# TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, i) for i in os.listdir(PATH_TO_TEST_IMAGES_DIR)]

# Size, in inches, of the output images.
IMAGE_SIZE = (19, 11)

# Params for analytic formula
w_b = np.random.normal(6, 2, 1) 
w_ch = np.random.normal(7, 2, 1)
w_old = np.random.normal(8, 2, 1)
w_r = np.random.normal(6, 2, 1)

client_coefs = {
    'w_b': w_b,
    'w_ch': w_ch,
    'w_old': w_old,
    'w_r': w_r
}

V_p = 1.2
t1 = 3