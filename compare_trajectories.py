
from matplotlib import pyplot as plt
import trajectory as traj

if __name__ == '__main__':
    u_list = [20, 40, 60]
    theta = 45

    for u in u_list:
        traj.draw_trajectory(u, theta)

    # Add legend and show plot
    plt.legend(["{} m/s".format(u) for u in u_list])
    plt.show()
