import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np


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
    rectangle = plt.Rectangle((x[i],y[i]), -180, -270, angle=180.0, fill= False,ec="red")
    #rect = patches.Rectangle((x[i],y[i]),-180,-270,linewidth=1,edgecolor='r',facecolor='none')
    #ax.add_patch(rectangle)
    plt.gca().add_patch(rectangle)
    plt.scatter(500, 700, s=100)


plt.show()