# GreenIntervalPredicting
Current repository represents method for calculating optimal duration of green interval based on object detection of crossing road pedestrians

# Structure

1. <b>Notebooks</b> - there are 3 notebooks, which consist all necessary code for:
  a. Preprocessing images and data (DataProcessing.ipynb)
  b. Formula and it description  for calculating optimal green interval (GreenIntervalCalculation.ipynb)
  c. Full pipeline with object detection of pedestrians and calculating optimal green interval (GreenIntervalCalculationFullPipeline.ipynb)
2. <b>ObjectDetectionResults</b> - some results of working object detection algorithm for detecting: Pedestrians, Non-Pedestrians and Road
3. <b>Metrics</b> - current folder consist all metrics and graphs, which depict how does object detection algorithm work  
4. <b>Data</b> - current folder  consist full, train annotation and label map of object detection algorithm

# Dependencies

1. </b>Tensorflow Object Detection API</b> (https://github.com/tensorflow/models/tree/master/research/object_detection). Full process of setting up you can find in <b>GreenIntervalCalculationFullPipeline.ipynb</b> notebook
2.  <b>Tensorflow</b> < 2 version

# Train on your own data

If you want to train on your own data: 
- Fill Train and Test folders on Data 
- Create your own annotation files
All process of training and creating annotatio files you can find in <b>GreenIntervalCalculationFullPipeline.ipynb</b> notebook

# Model

Inference graph you can find [here](https://drive.google.com/drive/folders/19McKlvEA2NohkTKk9AGlfo9MX2TWyYWT?usp=sharing).
How to test current inference graph you can find in <b>GreenIntervalCalculationFullPipeline.ipynb</b> notebook

## Metrics

### PEDESTRIANS 

![Preceision-Recall Curve For Pedestrian class](https://github.com/maikReal/GreenIntervalPredicting/blob/master/Metrics/Pedestrian.png)

<b>Average mAp</b> = 99.11%

### NON-PEDESTRIANS 

![Preceision-Recall Curve For Non-Pedestrian class](https://github.com/maikReal/GreenIntervalPredicting/blob/master/Metrics/Non-Pedestrian.png)

<b>Average mAp</b> = 83.27%

### ROAD

![Preceision-Recall Curve For Road class](https://github.com/maikReal/GreenIntervalPredicting/blob/master/Metrics/Road.png)

<b>Average mAp</b> = 95.44%

# TODO

1. Web app for demo and testing
2. Dockerfile for this web app


