import pandas as pd
import numpy as np
from config import *
from predict_pedestrians import PedestrianDetector

def green_interval_formula(number_of_people):

    res = params['t1'] + params['B'] / params['V_p'] + np.log(number_of_people + 1) * number_of_people + \
                params['w_b'] * params['isCrowdy'] + params['w_ch'] * params['isManyChildren'] + \
                params['w_old'] * params['isManyElders'] + params['w_r'] * params['isManyCars']

    return res

def calculate_green_interval(image_path):
    """
    Calculating green interval using formula.
    PEDESTRIAN --> 1
    NON-PEDESTRIAN --> 2
    ROAD --> 3

    :param image_path: !!! Should be list !!!
    :return:
    """
    detector = PedestrianDetector()

    detector_results = detector.get_image_detections(image_path)

    intervals = []
    for result in detector_results:

        detections_number = result['num_detections']

        classes = result['detection_classes'][:detections_number]

        number_of_pedestrians = np.where(classes == 1)[0].shape[0]

        interval = green_interval_formula(number_of_pedestrians)

        intervals.append(interval)

    return intervals


if __name__ == '__main__':
    img = 'data/TestImages/image_pedestrian_20.jpg'

    print(calculate_green_interval([img]))


