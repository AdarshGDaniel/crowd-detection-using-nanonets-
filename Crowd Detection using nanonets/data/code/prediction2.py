import requests, os, sys
import re
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')
image_path = sys.argv[1]

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/'

data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

Data_Split = (response.text).split(",")
count = 0  
data=[]
a=[]
x=[]
y=[]
k=[]
for i in range(len(Data_Split)):
    if 'label' in Data_Split[i]:
        count+=1
        for o in range(1,6,1):
            data.append(Data_Split[i+o]) 
for p in data:        
    a.append(re.findall(r"\d+",p))
print("Xmin:")
for p in range(0,len(a),5):
    x.append(a[p])
    print(a[p])
print("Ymin:")
for p in range(1,len(a),5):
    y.append(a[p])
    print(a[p])  
'''print("Xmax:")
for p in range(2,len(a),5):
    x.append(a[p])
    print(a[p])
print("Ymin:")
for p in range(3,len(a),5):
    y.append(a[p])
    print(a[p])  '''
print("Score")
for p in range(4,len(a),5):
    k.append(a[p])
    print(a[p])         




#im = np.array(Image.open('/Users/adarshgdaniel/Desktop/nano/nanonets-pedestrian-detection/images/88.jpg'), dstr=np.uint8)

#fig,ax = plt.subplots(1)

#ax.imshow(im)
# To disply text 
#plt.text(50, 90, "Hello This is 90% ", fontsize=12)
# Create a Rectangle patch
#rect = patches.Rectangle((50,100),200,200,linewidth=1,edgecolor='r',facecolor='none')

#ax.add_patch(rect)


#plt.show()