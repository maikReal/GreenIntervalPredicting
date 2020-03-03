import os

PATH_TO_FROZEN_GRAPH = 'data/Inference_graph/frozen_inference_graph.pb'
PATH_TO_LABELS = 'data/label_map.pbtxt'
NUM_CLASSES = 3 # PEDESTRIAN, NON-PEDESTRIAN, ROAD

TEST_IMAGES_PATH = os.path.join('data/TestImages')

RESULTS_PATH = os.path.join('results')

# parameters for calculating of green interval
params = {
    'w_b': 8.4,
    'w_ch': 3.7,
    'w_old': 6.3,
    'w_r': 3.7,
    'V_p': 1.2,
    'isCrowdy': 0,
    'isManyChildren': 0,
    'isManyElders': 0,
    'isManyCars': 0,
    't1': 3,
    'B': 18
}