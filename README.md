
# Multimodel Object and Pose Detector

- This notebook contains the code for Object Detector and Pose Detector

- The paths of the models have to be specified in the second block of the notebook (currently the relative paths of the models have already been set according to repository structure)

- The object detector uses ssdlite_mobilenet_v2 model and the pose detector used human-pose-estimation-0001.

- The object detector detects a person and idetifies it as a region of interest, this frame is cropped and sent to the pose detector to avoid processing of redundant pixels

- Currently the models are working independetly but after adding the exexution block in an asynchronous loop those models will work concurrently