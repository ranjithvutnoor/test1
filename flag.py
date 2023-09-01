import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
a = patch.Rectangle((0,1),width=9, height=2,facecolor = "#138808",edgecolor='grey')
b = patch.Rectangle((0,3),width=9, height=2,facecolor = "#ffffff",edgecolor='grey')
c = patch.Rectangle((0,5),width=9, height=2,facecolor = "#FF6103",edgecolor='grey')
m,n = plt.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

radius = 2
plt.plot(9,3,marker='o',markerfacecolor="#000080",markersize=9.5)
chakra = plt.Circle((4.5,4),radius,color='#000080',fill=False,linewidth=7)
n.add_patch(chakra)

for i in range(0, 24):
    angle = np.deg2rad(i * 15)  # Convert degrees to radians
    x = 4.5 + radius * np.cos(angle)
    y = 4 + radius * np.sin(angle)
    n.add_patch(patch.Polygon([[4.5, 4], [x, y], [x, y], [x, y]], fill=True, closed=True, color='#000080'))

plt.axis('equal')
plt.show()