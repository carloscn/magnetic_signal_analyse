#,coding,:,utf-8
# /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math

x_hz= np.array([15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,120,140,160,180,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000])
y_mv= np.array([50,78,182,270,426,604,784,940,1140,1440,1760,2020,2200,2140,1940,1720,1500,1280,728,520,420,356,312,236,204,168,136,122,108,99,88,77,76,71,66,64,61,59,53])

x_hz_c = np.array([15, 20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,120,140,160,180,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000])
x_mv_c = np.array([17, ])

# magnetic gain:
y_mv = y_mv / max(y_mv)
for i in range(len(y_mv)):
    y_mv[i] = 20*math.log10(y_mv[i])

# line:
line_x = np.linspace(1,200)
line_y = line_x *0 + -3;
print(line_x)
print(line_y)
plt.plot(x_hz,y_mv,'o-',label='mag', linewidth=2, markersize=4)
plt.plot(line_x, line_y, '--')
plt.text(150, -2.5, '-3dB', fontsize=15)
xdata, ydata = 5, 0


offset = 28
bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(
    arrowstyle = "->",
    connectionstyle = "angle,angleA=0,angleB=90,rad=10")

plt.annotate('data = (%.1fHz, %.1fdB)'%(62  , -3.0),
            (62  , -2.9), xytext=(offset*5, offset*-1), textcoords='offset points',
            bbox=bbox, arrowprops=arrowprops)

plt.annotate('data = (%.1fHz, %.1fdB)'%(90.608  , -3.0),
            (92  , -2.9), xytext=(offset*5, offset), textcoords='offset points',
            bbox=bbox, arrowprops=arrowprops)

plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Coil Sweep Frequency')
plt.grid(1)
plt.show()