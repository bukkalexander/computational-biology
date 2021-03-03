import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def u_s_0(s, s0, u0):
    """
    Initial population ramp up function
    """
    val = u0 / (1 + np.exp(s-s0))
    return val


def spatial_spread(u0, s0, p, q, s_start, s_stop, s_step, t_start, t_stop, t_step):
    s_array = np.arange(s_start, s_stop + s_step, s_step)
    s_len = len(s_array)
    t_array = np.arange(t_start, t_stop + t_step, t_step)
    t_len = len(t_array)

    u_array = np.zeros([s_len, t_len])
    du_dt_array = np.zeros([s_len, t_len])
    for i_s, s in zip(range(s_len), s_array):
        i_t = 0
        u_array[i_s, i_t] = u_s_0(s, s0, u0)

    # Simulate
    # Use boundary condition:
    #   the change in population with respect to x in
    #   u(0, t) and u(L, t) is equal to zero, which is
    #   why we should skip the first and last value in s_array
    #   (i.e. 1 and 100) when we simulate.

    for i_t in range(t_len - 1):
        for i_s, s in zip(range(s_len), s_array):
            u = u_array[i_s, i_t]
            if s == s_start:
                diffusion = (u_array[i_s + 1, i_t] - u) / s_step**2
            elif s == s_stop:
                diffusion = (u_array[i_s - 1, i_t] - u) / s_step**2
            else:
                diffusion = (u_array[i_s + 1, i_t] + u_array[i_s - 1, i_t] - 2 * u) / s_step ** 2
            du_dt_array[i_s, i_t + 1] = p * u * (1 - u / q) - u / (1 - u / q) + diffusion
            u_array[i_s, i_t + 1] = u_array[i_s, i_t] + t_step * du_dt_array[i_s, i_t + 1]
    return u_array, du_dt_array


def problem_1_b():
    print('Problem 1 (b)')

    p = 0.5
    q = 8

    s_start = 1.0
    s_stop = 100.0
    s_step = 1.0
    s_array = np.arange(s_start, s_stop + s_step, s_step)

    t_start = 0.0
    t_stop = 300
    t_step = 0.01
    t_array = np.arange(t_start, t_stop + t_step, t_step)

    u_steady = [
        0,
        -(1 - q) / 2 + np.sqrt((1 - q) ** 2 / 4 - (q / p - q)),
        -(1 - q) / 2 - np.sqrt((1 - q) ** 2 / 4 - (q / p - q))
    ]

    # (i)
    # s0 = 20
    # u0 = u_steady[1]

    # (ii)
    s0 = 50
    u0 = u_steady[2]

    # # (iii)
    # s0 = 50
    # u0 = u_steady[2]*1.1

    u_array, du_dt_array = spatial_spread(u0, s0, p, q, s_start, s_stop, s_step, t_start, t_stop, t_step)


    # Plots solution space
    fig = plt.figure()
    ax_solution_space = plt.subplot(2, 2, 1)
    line_solution_space, = plt.plot(s_array, u_array[:, 0])

    plt.title(r'Solution space')
    plt.xlabel(r'$s$ [position]')
    plt.ylabel(r'$u(s, t)$ [population]')

    # Plot phase space
    v_array = u_array[1:, :] - u_array[0:-1, :]

    ax_phase_space = plt.subplot(2, 2, 2)
    line_phase_space, = plt.plot(u_array[1:, 0], v_array[:, 0])

    plt.title(r'Phase space')
    plt.xlabel(r'$u(s, t)$ [population]')
    plt.ylabel(r'$v$ [position/time]')

    ax_slider = plt.axes([0.1, 0.05, 0.8, 0.05])
    # here we create the slider
    a_slider = Slider(ax_slider,  # the axes object containing the slider
                      'i_t',  # the name of the slider parameter
                      t_start,  # minimal value of the parameter
                      len(t_array)-1,  # maximal value of the parameter
                      valinit=t_start  # initial value of the parameter
                      )

    def update(t):
        # Solution space
        line_solution_space.set_ydata(u_array[:, int(t)])
        ax_solution_space.axis((s_array.min(), s_array.max(),
                                u_array[:, int(t)].min(), u_array[:, int(t)].max() * 1.05))
        plt.title('t = ' + str(t_array[int(t)]))

        # Phase space
        line_phase_space.set_xdata(u_array[1:, int(t)])
        line_phase_space.set_ydata(v_array[:, int(t)])
        # line_fixed_point.set_xdata([N.min(), N.max()])
        # line_fixed_point.set_ydata([0, 0])
        ax_phase_space.axis((u_array[:, int(t)].min(), u_array[:, int(t)].max() * 1.05,
                             v_array[:, int(t)].min(), v_array[:, int(t)].max() * 1.05))

        # redraw the plot
        fig.canvas.draw_idle()

    a_slider.on_changed(update)
    plt.show()

    # # (ii)

    # u_array, du_dt_array = spatial_spread(u0, s0, p, q, s_start, s_stop, s_step, t_start, t_stop, t_step)
    # plt.plot(s_array, u_array[:, 0])
    print('Done: Problem 1 (b)')


def main():
    problem_1_b()


if __name__ == "__main__":
    main()
