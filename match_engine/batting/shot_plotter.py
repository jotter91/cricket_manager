import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv


class Shot:
    def r(self, theta):
        """return the maximum radius expected for the shot as a function of angle
        where the angle is defined between the popping crease and shot
        theta : angle in radians

        returns radius in metres
        """
        return 1.0

    def probability(self, line, height):
        """
        return the probability of successfully executing the shot

        :param y: line in metres
        :param z: height at batting plane in metres
        :return: probabilty as a float between 0 and 1
        """
        return 1.0


class CoverDrive(Shot):
    def probability(self, line, height):
        centre = (0.56, 0.32)
        radius = 0.2
        a = 30.0

        delta = np.sqrt((line - centre[0]) ** 2.0 + (height - centre[1]) ** 2.0)
        #if delta < radius:
        return np.exp(-a * delta ** 2)
        #else:
        #    return 0.0

    def r(self, theta):
        if 0 < theta < np.pi:
            r = 0
        elif np.pi< theta < np.pi+1.4:
            r = 80
        else:
            r=0
        return r

class Leave(Shot):
    def probability(self, line, height):
        return 1.0

    def r(self,theta):
        return 0

ALL_SHOTS = [CoverDrive,Leave]

if __name__ =="__main__":
    stump_width = 0.2286
    max_line = 4 * stump_width
    stump_height = 0.711

    height = np.linspace(0, 2, 200)
    line = np.linspace(max_line, -stump_width, 200)

    cover_drive_obj = CoverDrive()
    cover_drive = np.zeros((200, 200))
    for i in range(200):
        for j in range(200):
            cover_drive[j][i] = cover_drive_obj.probability(line[i], height[j])

    to_plot = [cover_drive, ]
    fig, axs = plt.subplots(1, 2)
    for z_plot in to_plot:
        ax = axs[0]
        i = ax.contourf(line, height, z_plot, cmap=cm.jet)
        fig.colorbar(i)

        ax.plot([0.0, 0.0], [0.0, stump_height], color='k', linestyle='-', linewidth=5)
        ax.plot([0.5 * stump_width, 0.5 * stump_width], [0.0, stump_height], color='k', linestyle='-', linewidth=5)
        ax.plot([stump_width, stump_width], [0.0, stump_height], color='k', linestyle='-', linewidth=5)

        ax.plot([0, stump_width], [stump_height, stump_height], color='k', linestyle='-', linewidth=5)
        ax.invert_xaxis()
        ax.set_aspect(1.0)

    ax = axs[1]
    for x in [10.12, -10.12]:
        ax.plot([-1.32, 1.32], [x, x], 'g')
    ax.plot([-1.32, -1.32], [10.12, -10.12], 'g')
    ax.plot([1.32, 1.32], [10.12, -10.12], 'g')
    theta = np.linspace(0, 2 * np.pi, 100)
    x = 70 * np.cos(theta)
    y = 70 * np.sin(theta)
    ax.plot(x, y, 'k')
    cover_drive_x = np.zeros(100)
    cover_drive_y = np.zeros(100)
    for i in range(100):
        r = cover_drive_obj.r(theta[i])
        cover_drive_x[i] = r * np.cos(theta[i])
        cover_drive_y[i] = r * np.sin(theta[i])+ (10.12-1.22) ##offset to popping crease

    ax.plot(cover_drive_x, cover_drive_y, 'b')

    ax.set_aspect(1.0)
    plt.show()
