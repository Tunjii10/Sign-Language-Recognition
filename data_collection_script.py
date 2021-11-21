import os
import cv2
import time
import uuid
import matplotlib.pyplot as plt

image_save = r"Tensorflow\workspace\training_demo\images"

labels = ["I", "My", "You", "Father", "Mother", "How", "Name", "Smile", "Hello", "Morning", "Night", "Afternoon" ]
number_imgs = 1


for x in labels:
	cap = cv2.VideoCapture(0)
	preframe_tm = time.time()
	i = 0
	while True:
		ret, frame = cap.read()
		elapsed_time = time.time() - preframe_tm
		if elapsed_time < 6:
			preframe_tm = time.time()
			i += 1
			print("Taken image {}-{}".format(x,i))
			imgname = os.path.join(image_save,x+'.'+'{}.jpg'.format(str(uuid.uuid1())))
			cv2.imwrite(imgname, frame)
			time.sleep(3)
			if i >= number_imgs:
				break
			
	cap.release()
	cv2.destroyAllWindows()
