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
xmin=[]
ymin=[]
xmax=[]
ymax=[]
kscore=[]

for i in range(len(Data_Split)):
    if 'label' in Data_Split[i]:
        count+=1
        for o in range(1,6,1):
            data.append(Data_Split[i+o]) 
for p in data:        
    a.append(re.findall(r"\d+",p))

print("Xmin:")
for p in range(0,len(a),5):
    xmin.append(a[p])

print("Ymin:")
for p in range(1,len(a),5):
    ymin.append(a[p])


print("Xmax:")
for p in range(2,len(a),5):
    xmax.append(a[p])
print("Ymin:")
for p in range(3,len(a),5):
    ymax.append(a[p])


print("Score")
for p in range(4,len(a),5):
    kscore.append(a[p])

j=[]
t=[]

for i in range(len(xmax)):
    j.append(xmax[0]-xmin[0])
    t.append(ymax[0]-ymin[0])


print(j)
print(t)


'''
x=[500,800,300,400]
y=[700,400,999,666]
s=[80,90,20,60]



im = np.array(Image.open('/Users/adarshgdaniel/Desktop/nano/3.jpg'), dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)


for i in range(len(x)):
    # To disply text
    plt.text(x[i]-10, y[i]-10, s[i], fontsize=12)
    # Create a Rectangle patch
    rect = patches.Rectangle((x[i],y[i]),180,270,linewidth=1,edgecolor='r',facecolor='none')
    ax.add_patch(rect)


plt.show()'''

