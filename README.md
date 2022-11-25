# Nested Image Classification using MobileNet V2 and Resnet-50 using Intel OpenVINO Runtime Tools
  
A nested model image classifier which performs dual functionality of identifying the object and classifying the object identified
We have utilised the OpenVINO runtime tools for this
It utilises the pretrained models from the OpenVINO Model zoo:

1.MobileNetV2: https://docs.openvino.ai/latest/omz_models_model_ssdlite_mobilenet_v2.html
This model performs the object detection task in our classifier and is trained to identify objects on the set amount of classes.

2.Resnet-50 https://docs.openvino.ai/latest/omz_models_model_resnet_50_tf.html#doxid-omz-models-model-resnet-50-tf
This model perfoms the task of classifying the object identified by model 1.
