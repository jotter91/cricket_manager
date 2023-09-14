import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
import csv 

#bowling grid taken from page 99 of hitting against the spin 

X = 100*np.random.rand(6,6)


#stumps are 22.86cm wide and 71.1cm high - Appendix D Law 8 of the MCC laws
#all dimensions in metres
stump_width=0.2286 
stump_height = 0.711 
stump_diameter= 0.0381 

#line - stump region is split into 4 , so each grid is 
del_line = stump_width/4


#zero at leg stump 14 blocks from leg stump to offisde, then one final big block, one small block to the leg side and one 3* block 
max_line = 4*stump_width


line = [max_line, max_line-2*del_line, max_line -3*del_line, max_line - 4*del_line, #end of wide region
        max_line -5*del_line,max_line -6*del_line,max_line -7*del_line,max_line -8*del_line, #end of offside region 
        max_line -9*del_line,max_line -10*del_line,max_line -11*del_line,max_line -12*del_line, #end of channel
        max_line -13*del_line,max_line -14*del_line,max_line -15*del_line,max_line -16*del_line, #end of stumps
        max_line -17*del_line,max_line -20*del_line # end of legside
        ]
line = np.linspace(max_line,-stump_width,20)
print(line)
print(len(line))
assert (max(line) - max_line) <0.001
assert (min(line) - -stump_width) < 0.001
assert len(line) ==20
#length is split into 0.5 metre chunks
pitch_length = 20.12 
pitch_width = 3.05 

pitch_limit = 12.0 
#length of 0 is at batters stumps

length = np.linspace(0,pitch_limit, 25)
print(length)

line_grid,length_grid =np.meshgrid(line,length)
economy_rate = np.zeros((25,20))
batting_avg = np.zeros((25,20))


#batting plane grids
height = np.linspace(0,2,20)
print(height)

economy_rate_height = np.zeros((20,20))
batting_avg_height = np.zeros((20,20))

#start at top left i.e. wide offside region and length of zero 
"""
economy_rate[0][0] = 3.1 
economy_rate[1][0] = 3.1 
economy_rate[2][0] = 6.1 
economy_rate[3][0] = 8.8 

economy_rate[4][0] = 9.5 
economy_rate[5][0] = 10.2 
economy_rate[6][0] = 11.7
economy_rate[7][0] = 10.0

economy_rate[8][0] = 6.5 
economy_rate[9][0] = 5.2 
economy_rate[10][0] = 5.4
economy_rate[11][0] = 4.8

economy_rate[12][0] = 6.0 
economy_rate[13][0] = 6.1 
economy_rate[14][0] = 6.7
economy_rate[15][0] = 7.1

economy_rate[16][0] = 8.2 
economy_rate[17][0] = 7.4 
economy_rate[18][0] = 7.4
economy_rate[19][0] = 7.4
"""
with open('economy_rate.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        for i,item in enumerate(row):
            economy_rate[line_count][i] = item
        line_count += 1

with open('batting_average.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        for i,item in enumerate(row):
            batting_avg[line_count][i] = item
        line_count += 1

print(economy_rate)
text_kwargs = dict(ha='center', va='center', fontsize=10, color='k')
to_plot=[economy_rate,batting_avg]
fig, axs = plt.subplots(1,2)
bounds = [np.arange(0,7,0.5),np.arange(0,100,5)]
labels=['Economy Rate','Batting Average']
for i,z_plot in enumerate(to_plot):
    ax = axs[i]
    bound =bounds[i]
    label=labels[i]
    ax.set_title(label)
    i = ax.contourf(line,length,z_plot,bound,cmap=cm.jet,extend='both')
    fig.colorbar(i)
    ax.scatter(0,0,marker='o',s=50,c='k')
    ax.scatter(11.43e-2,0,marker='o',s=50,c='k')
    ax.scatter(22.86e-2,0,marker='o',s=50,c='k')

    for i in [-1,0,1,2,3]:
        ax.plot([i*stump_width,i*stump_width],[0,pitch_limit],color='k',linestyle='--')
    ax.plot([-1*stump_width,4*stump_width],[1.22,1.22],color='k',linestyle='-')

    ax.text(3.5*stump_width, 0.2, 'Wide', **text_kwargs)
    ax.text(2.5*stump_width, 0.2, 'Offside', **text_kwargs)
    ax.text(1.5*stump_width, 0.2, 'Channel', **text_kwargs)
    ax.text(0.5*stump_width, 0.2, 'Stumps', **text_kwargs)
    ax.text(-0.5*stump_width, 0.2, 'Legside', **text_kwargs)

    ax.text(5*stump_width, 4, 'Half-Volley',rotation='vertical', **text_kwargs)
    ax.text(5*stump_width, 5.5, 'Full',rotation='vertical', **text_kwargs)
    ax.text(5*stump_width, 7, 'Good',rotation='vertical', **text_kwargs)
    ax.text(5*stump_width, 8.5, 'Heavy',rotation='vertical', **text_kwargs)
    ax.text(5*stump_width, 10.0, 'Short',rotation='vertical', **text_kwargs)

    ax.plot([-1*stump_width,4*stump_width],[3.,3.],color='k',linestyle='--')
    ax.plot([-1*stump_width,4*stump_width],[5.,5.],color='k',linestyle='--')
    ax.plot([-1*stump_width,4*stump_width],[6.,6.],color='k',linestyle='--')
    ax.plot([-1*stump_width,4*stump_width],[8.,8.],color='k',linestyle='--')
    ax.plot([-1*stump_width,4*stump_width],[9.,9.],color='k',linestyle='--')
    ax.plot([-1*stump_width,4*stump_width],[11.,11.],color='k',linestyle='--')

    ax.set_aspect(0.25)
    ax.invert_xaxis()
    ax.invert_yaxis()
#plt.show()

#now look at batting plane
with open('economy_rate_height.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        for i,item in enumerate(row):
            economy_rate_height[line_count][i] = item
        line_count += 1
with open('batting_average_height.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        for i,item in enumerate(row):
            batting_avg_height[line_count][i] = item
        line_count += 1
fig, axs = plt.subplots(1,2)
to_plot = [economy_rate_height,batting_avg_height]
for i,z_plot in enumerate(to_plot):
    ax=axs[i]
    label=labels[i]
    bound=bounds[i]
    ax.set_title(label)
    i = ax.contourf(line, height, z_plot,bound, cmap=cm.jet, extend='both')
    cbar = fig.colorbar(i)
    ax.plot([0.0,0.0],[0.0,stump_height],color='k',linestyle='-',linewidth=5)
    ax.plot([0.5*stump_width,0.5*stump_width],[0.0,stump_height],color='k',linestyle='-',linewidth=5)
    ax.plot([stump_width,stump_width],[0.0,stump_height],color='k',linestyle='-',linewidth=5)
    ax.plot([0,stump_width],[stump_height,stump_height],color='k',linestyle='-',linewidth=5)


    ax.text(3.5 * stump_width, 1.8, 'Wide', **text_kwargs)
    ax.text(2.5 * stump_width, 1.8, 'Offside', **text_kwargs)
    ax.text(1.5 * stump_width, 1.8, 'Channel', **text_kwargs)
    ax.text(0.5 * stump_width, 1.8, 'Stumps', **text_kwargs)
    ax.text(-0.5 * stump_width, 1.8, 'Legside', **text_kwargs)


    for i in [-1, 0, 1, 2, 3]:
        ax.plot([i * stump_width, i * stump_width], [0, 2.0], color='k', linestyle='--')
    ax.invert_xaxis()
    ax.set_aspect(1.0)
plt.show()