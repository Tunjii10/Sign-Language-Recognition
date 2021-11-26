# Sign-Language-Recognition

## Description
This repo involves the  use of tensorflow object detection API to build a custom sign language recognizer. For this project I focused on few words,verbs,pronouns and greetings in the Nigerian Sign Language. 

## Steps
All steps followed are available [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html) the tensorflow object detection API docs.


I collected my data from my webcam with the script
```python
python data_collection_script.py
```

For automatic label Map generation. Edit the labelMap.py file according to your different labels. Then run
```python
python labelMap.py
``` 

For detecting sign language with webcam
```python
python webcam_detection.py
``` 

## Improvements 
-Increasing the no. of steps 
-Using a better and different model 