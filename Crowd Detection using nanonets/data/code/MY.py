import requests, os, sys
import re , json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import cv2
import numpy as np

model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')
#image_path = sys.argv[1]
vid = cv2.VideoCapture("/Users/adarshgdaniel/Downloads/vid.mp4")

url = ('https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/')

while True:  
    
    image= vid.read()
    data = {'file': image,    'modelId': ('', model_id)}

    #data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

    response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

    json_data = response.json()
    im = np.array(image, dtype=np.uint8)


    #im = np.array(Image.open('/Users/adarshgdaniel/Desktop/nano/nanonets-pedestrian-detection/88.jpg'), dtype=np.uint8)
    fig,ax = plt.subplots(1)
    ax.imshow(im)

    results = json_data['result']
    here = results[0]
    resultsa = here['prediction']
    for i in resultsa:
        herea = i
        x = herea['xmin']
        y = herea['ymin']
        s = herea['score']
        s=int(s*100)
        print(x," ",y)
        plt.text(x-10, y-5, s, fontsize=8)
        rectangle = plt.Rectangle((x,y), -50, -100, angle=180.0, fill= False,ec="red")
        #rect = patches.Rectangle((x[i],y[i]),-180,-270,linewidth=1,edgecolor='r',facecolor='none')
        #ax.add_patch(rectangle)
        plt.gca().add_patch(rectangle)

    plt.show()
