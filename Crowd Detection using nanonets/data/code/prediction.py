#before running this program plese use terminal to run the following commands(should be within the project folder)

#export NANONETS_API_KEY=Wzqi3cwoOBXP_T5KKaHoCavBmw6tvwWb
#export NANONETS_MODEL_ID=eedd33cf-b149-4f22-989e-fd55f3a8993a

import requests, os, sys
import re , json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import cv2
import numpy as np


model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')

image_path = sys.argv[1]

url = ('https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/')

data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

json_data = response.json()

#specify your path here!
#this image is to disply with all the plots
#replace this example path with your path to the image you want to display 

im = np.array(Image.open('/Users/admin/Desktop/nano/nanonets-pedestrian-detection/images/88.jpg'), dtype=np.uint8)
fig,ax = plt.subplots(1)
ax.imshow(im)

results = json_data['result']
here = results[0]
resultsa = here['prediction']

#for loop to plot the points on the detected people!

for i in resultsa:
    herea = i
    x = herea['xmin']
    y = herea['ymin']
    s = herea['score']
    s=int(s*100)
    print(x," ",y)
    plt.text(x-10, y-5, s, fontsize=8)
    rectangle = plt.Rectangle((x,y), -50, -100, angle=180.0, fill= False,ec="red")
    plt.gca().add_patch(rectangle)

plt.show()
