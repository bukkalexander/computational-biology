import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


def p_1_a():
    # ==================================================================================================================
    #    Define parameters
    # ==================================================================================================================

    # Time parameter
    t_start = 0.0
    t_step_size = 0.01
    t_end = 100.0
    t_array = np.arange(t_start, t_end, t_step_size)
    n_t = len(t_array)

    # Delayed time parameter
    T_start = 0.1
    T_step_size = 0.1
    T_end = 5.0
    T_array = np.arange(T_start, T_end, T_step_size)
    n_T = len(T_array)

    # Growth rate
    r = 0.1

    # Carrying capacity
    K = 100

    # Allee effect
    A = 20

    # Initial condition at t=0
    N_0 = 50

    # Assume N(t) = N_0 for [-T, 0] =>
    N_delay_0 = N_0

    # ==================================================================================================================
    #    Calculate values for N_dot for all T in T_array, for t in t_array
    # ==================================================================================================================
    # Initialize N_dot, N and N_delay to initial conditions
    N_dot = np.zeros([n_T, n_t])
    N = np.zeros([n_T, n_t])
    N[:, 0] = N_0

    for i_T in range(n_T):
        N_delay = N_0
        for i_t in range(n_t - 1):
            if t_array[i_t] - T_array[i_T] > 0.0:
                i_delay = int(T_array[i_T] / t_step_size)
                N_delay = N[i_T, i_t - i_delay]
            N_dot[i_T, i_t + 1] = r*N[i_T, i_t] * (1 - N_delay/K) * (N[i_T, i_t]/A - 1)
            N[i_T, i_t + 1] = N[i_T, i_t] + t_step_size*N_dot[i_T, i_t + 1]

    # Plot N as a function of t for all T
    fig, ax = plt.subplots()

    plt.xlabel(r'$t$ [time]')
    plt.ylabel(r'$N(t)$ [population]')
    for i_T in range(n_T):
        # plt.clf()
        plt.title(r'$N(t)$, $T=' + str(T_array[i_T] )+ r'$')
        plt.xlabel(r'$t$ [time]')
        plt.ylabel(r'$N(t)$ [population]')
        plt.plot(t_array, N[i_T, :])
    # plt.show()

    # Bifurcation diagram
    fig_bifurcatio, ax_bifurcation = plt.subplots()
    plt.plot(T_array, N[:, 9000:])
    print('h')


def p_1_b():
    # ==================================================================================================================
    #    Define parameters
    # ==================================================================================================================

    # Time parameter
    t_start = 0.0
    t_step_size = 0.001
    t_end = 100.0
    t_array = np.arange(t_start, t_end, t_step_size)
    n_t = len(t_array)

    # Time delayed  parameter
    T_start = 0.1
    T_step_size = 0.001
    T_end = 6.0
    T_array = np.arange(T_start, T_end, T_step_size)
    n_T = len(T_array)

    # Growth rate
    r = 0.1

    # Carrying capacity
    K = 100

    # Allee effect
    A = 20

    # Initial condition at t=0
    N_0 = 50

    # Assume N(t) = N_0 for [-T, 0] =>
    N_delay_0 = N_0

    # ==================================================================================================================
    #    Calculate values for N_dot for all T in T_array, for t in t_array
    # ==================================================================================================================
    def get_population(T):
        # Initialize N_dot, N and N_delay to initial conditions
        N_dot = np.zeros([n_t])
        N = np.zeros([n_t])
        N[0] = N_0
        N_delay = N_0
        for i_t in range(n_t - 1):
            if t_array[i_t] - T > 0.0:
                i_delay = int(T / t_step_size)
                N_delay = N[i_t - i_delay]
            N_dot[i_t + 1] = r * N[i_t] * (1 - N_delay / K) * (N[i_t] / A - 1)
            N[i_t + 1] = N[i_t] + t_step_size * N_dot[i_t + 1]
        return N_dot, N
    T = T_array[0]
    N_dot, N = get_population(T)

    # Plots
    fig = plt.figure()

    # Phase space
    ax_phase_space = plt.subplot(2, 2, 1)
    line_phase_space, = plt.plot(N, N_dot)
    line_fixed_point, = plt.plot([N.min(), N.max()], [0, 0])

    plt.title(r'Phase space')
    plt.xlabel(r'$N$')
    plt.ylabel(r'$\dot{N}$')

    # Solution space
    ax_solution_space = plt.subplot(2, 2, 2)
    line_solution_space, = plt.plot(t_array, N)

    plt.title(r'Solution space')
    plt.xlabel(r'$t$ [time]')
    plt.ylabel(r'$N(t)$ [population]')

    ax_slider = plt.axes([0.1, 0.05, 0.8, 0.05])
    # here we create the slider
    a_slider = Slider(ax_slider,  # the axes object containing the slider
                      'T',  # the name of the slider parameter
                      T_array[0],  # minimal value of the parameter
                      T_array[-1],  # maximal value of the parameter
                      valinit=T_array[0]  # initial value of the parameter
                      )

    def update(T):
        N_dot, N = get_population(T)

        # Phase space
        line_phase_space.set_xdata(N)
        line_phase_space.set_ydata(N_dot)
        line_fixed_point.set_xdata([N.min(), N.max()])
        line_fixed_point.set_ydata([0, 0])
        ax_phase_space.axis((N.min(), N.max()*1.05, N_dot.min(), N_dot.max()*1.05))

        # Solution space
        line_solution_space.set_xdata(t_array)
        line_solution_space.set_ydata(N)
        ax_solution_space.axis((t_array.min(), t_array.max(), N.min(), N.max() * 1.05))

        # redraw the plot
        fig.canvas.draw_idle()

    a_slider.on_changed(update)
    plt.show()


def problem_1():
    # p_1_a()
    p_1_b()


def main():
    problem_1()


if __name__ == "__main__":
    main()
