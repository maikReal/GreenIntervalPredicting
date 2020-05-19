from detection_graphs_fucntions import get_bbox_info, preprocess_output_data
import numpy as np
from config import *
from datetime import datetime


def calculate_optimal_time(file_path, road_width, mode='Image'):

    if mode == 'Image':
        output_bbox = get_bbox_info(file_path)
        prep_output_bbox = preprocess_output_data(output_bbox)[0]
        num_pedestrians = np.where(prep_output_bbox['classes'] == 1)[0].shape[0]

    if mode == 'Video':
        pass
    
    events_dict = get_events()

    # calculating green interval in seconds
    result = t1 + float(road_width) / V_p + np.log(num_pedestrians + 1) * num_pedestrians + \
                client_coefs['w_b'] * events_dict['isCrowdy'] + client_coefs['w_ch'] * events_dict['isManyChildren'] + \
                client_coefs['w_old'] * events_dict['isManyElders'] + client_coefs['w_r'] * events_dict['isManyCars']
    
    return result

def get_events():

    cur_hours = datetime.now().hour

    events_dict = {'isCrowdy': 0, 'isManyChildren': 0, 'isManyElders': 0, 'isManyCars': 0}

    if (cur_hours >= 8 and cur_hours <= 11) or (cur_hours >= 12 and cur_hours <= 15) or (cur_hours >= 18 and cur_hours <= 20):
        events_dict['isCrowdy'] = 1

    if cur_hours >= 12 and cur_hours <= 14:
        events_dict['isManyChildren'] = 1

    if cur_hours >= 7 and cur_hours <= 9:
        events_dict['isMnayElders'] = 1

    if (cur_hours >= 9 and cur_hours <= 10) or (cur_hours >= 17 and cur_hours <= 19):
        events_dict['isManyCars'] = 1

    return events_dict



