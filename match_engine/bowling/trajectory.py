import numpy as np 
from matplotlib import pyplot as plt

x_popping=1.22

def set_axes_equal(ax):
    """
    Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    """

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

def create_traj(release_point,release_velocity,release_acceleration):
    x_plot=[]
    y_plot =[]
    z_plot=[]
    del_t = 0.001 # seconds

    x,y,z=release_point

    vx,vy,vz=release_velocity

    ax,ay,az=release_acceleration
    
    x_new = x
    i =0
    while  i <600:
        x_new = x+vx*del_t
        y_new = y+vy*del_t
        z_new = z+vz*del_t

        vx_new =vx + ax*del_t
        vy_new =vy + ay*del_t
        vz_new =vz + az*del_t

        ax=0.0
        ay=0.0
        az=-9.81
        x_plot.append(x_new)
        y_plot.append(y_new)
        z_plot.append(z_new)
        #print(i,x_new,y_new,z_new)
        i+=1
        vx = vx_new
        vy = vy_new
        vz = vz_new
        x = x_new
        y = y_new
        z= z_new
        if z<0:
            #bounce
            vz = -0.95*vz
            #print('hit pitch',x,y,z,vz)
    return np.asarray(x_plot),np.asarray(y_plot),np.asarray(z_plot)

def interpolate_to_loc(x,y,z,target_loc,output_loc,loc):

    if target_loc=='x':
        array_1=x
    elif target_loc=='y':
        array_1=y
    else:
        array_1=z

    if output_loc == 'x':
        array_2 = x
    elif output_loc == 'y':
        array_2 = y
    else:
        array_2 = z

    index = (np.abs(array_1 - loc)).argmin()

    return array_2[index]



def calculate_drag_force():
    return 0  

def example_with_plot(theta):
    rp = (-20.12, 0.4, 2.0)
    v_mag = 35.8
    phi = 0  # angle between y and x

    rv = (v_mag * np.cos(np.deg2rad(theta)), 0.0, v_mag * np.sin(np.deg2rad(theta)))
    print(rv)
    ra = (0, 0, 0)

    x_plot, y_plot, z_plot = create_traj(rp, rv, ra)

    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    # Grab some test data.
    # ax.set_box_aspect((np.ptp(xs), np.ptp(ys), np.ptp(zs)))  # aspect ratio is 1:1:1 in data space

    # Plot a basic wireframe.
    ax.plot(x_plot, y_plot, z_plot)
    ax.scatter(x_plot[0], y_plot[0], z_plot[0], marker='o', color='purple')
    ax.scatter(x_plot[-1], y_plot[-1], z_plot[-1], marker='o', color='r')

    # add stumps
    stump_height = 0.711
    for x in [-20.12, 0]:
        ax.plot([x, x], [0.0, 0.0], [0.0, stump_height], color='k')
        ax.plot([x, x], [-11.43e-2, -11.43e-2], [0.0, stump_height], color='k')
        ax.plot([x, x], [-22.86e-2, -22.86e-2], [0.0, stump_height], color='k')
        ax.plot([x, x], [0, -22.86e-2], [stump_height, stump_height], color='k')

        # wicket
        ax.plot([x, x], [-1.32, 1.32], [0, 0], 'g')
    ax.plot([-20.12, 0], [-1.32, -1.32], [0, 0], 'g')
    ax.plot([-20.12, 0], [1.32, 1.32], [0, 0], 'g')

    ax.set_box_aspect([1, 1, 1])
    set_axes_equal(ax)
    plt.show()


def to_solve(alpha,*args):
    x,z,v = args

    return x*np.tan(alpha) - 0.5*9.81*(x**2)/(v*v*(np.cos(alpha))**2) -z

def hit_target_pitch(line,length,release_velocity,release_height=-2):

    #0print(to_solve(0,length,release_height,release_velocity))

    from scipy.optimize import fsolve
    return  fsolve(to_solve,np.deg2rad(-5),args=(length,release_height,release_velocity))





if __name__=="__main__":
    #example_with_plot(0)
    line= 0.3
    length =17.5
    velocity = 35
    angle = hit_target_pitch(line,length,velocity)
    print(angle)
    example_with_plot(np.rad2deg(angle))
    rp = (-20.12, line, 2.0)
    phi = 0  # angle between y and x

    rv = (velocity * np.cos(angle), 0.0, velocity * np.sin(angle))
    ra = (0, 0, 0)
    x,y,z = create_traj(rp,rv,ra)

    print(interpolate_to_loc(x,y,z,'z','x',0))
    print(interpolate_to_loc(x,y,z,'x','z',-1.22))
