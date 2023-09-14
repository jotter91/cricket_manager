import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv

stump_width=0.2286
max_line = 4*stump_width
stump_height = 0.711

height = np.linspace(0,2,20)
line = np.linspace(max_line,-stump_width,20)

#cover drive
centre = (0.56,0.32)
radius = 0.2

cover_drive = np.zeros((20,20))
a=10.0
for i in range(20):
    for j in range(20):
        delta =  np.sqrt( (line[i]-centre[0])**2.0 + (height[j]-centre[1])**2.0)
        if delta <radius:
            print(line[i],height[j],delta,i,j)
            cover_drive[j][i] = np.exp(-a*delta**2)

to_plot = [cover_drive,]
fig, axs = plt.subplots(1,2)
for z_plot in to_plot:
    ax = axs[0]
    i = ax.contourf(line, height, z_plot, cmap=cm.jet)
    fig.colorbar(i)

    ax.plot([0.0,0.0],[0.0,stump_height],color='k',linestyle='-',linewidth=5)
    ax.plot([0.5*stump_width,0.5*stump_width],[0.0,stump_height],color='k',linestyle='-',linewidth=5)
    ax.plot([stump_width,stump_width],[0.0,stump_height],color='k',linestyle='-',linewidth=5)

    ax.plot([0,stump_width],[stump_height,stump_height],color='k',linestyle='-',linewidth=5)
    ax.invert_xaxis()
    ax.set_aspect(1.0)

ax = axs[1]
for x in [10.12, -10.12]:
    ax.plot([-1.32, 1.32], [x, x],  'g')
ax.plot( [-1.32, -1.32],[10.12, -10.12], 'g')
ax.plot( [1.32, 1.32],[10.12, -10.12],  'g')
theta = np.linspace(0,2*np.pi,100)
x = 60*np.cos(theta)
y = 60*np.sin(theta)
ax.plot(x,y,'k')

ax.plot([0,-60],[10.12,10.12],'b')
ax.plot([-1.32,-40],[-10.12,-46],'b')



ax.set_aspect(1.0)
plt.show()
