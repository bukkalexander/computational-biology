import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


def problem_1():
    # p_1_a()
    p_1_c()


def p_1_a():
    # ==================================================================================================================
    #    Define parameters
    # ==================================================================================================================

    # Time parameter
    t_start = 0.0
    t_step_size = 0.001
    t_end = 100.0
    t_array = np.arange(t_start, t_end, t_step_size)
    n_t = len(t_array)

    # Delayed time parameter
    T_start = 1.0
    T_step_size = 0.1
    T_end = 2.0
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

    for i_T in range(n_T):
        plt.plot(t_array, N[i_T, :])
        plt.show()

    plt.show()


def p_1_c():
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

    fig = plt.figure()

    ax_N = plt.axes([0.1, 0.2, 0.8, 0.65])

    N_plot, = plt.plot(N, N_dot)
    fixed_point_line_plot, = plt.plot([N.min(), N.max()], [0, 0])

    plt.title(r'$\dot{N}$ vs $N$')
    plt.xlabel(r'$N$')
    plt.ylabel(r'$\dot{N}$')

    slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])
    # here we create the slider
    a_slider = Slider(slider_ax,  # the axes object containing the slider
                      'T',  # the name of the slider parameter
                      T_array[0],  # minimal value of the parameter
                      T_array[-1],  # maximal value of the parameter
                      valinit=T_array[0]  # initial value of the parameter
                      )

    def update(T):
        N_dot, N = get_population(T)
        N_plot.set_xdata(N)
        N_plot.set_ydata(N_dot)
        fixed_point_line_plot.set_xdata([N.min(), N.max()])
        fixed_point_line_plot.set_ydata([0, 0])
        ax_N.axis((N.min(), N.max()*1.05, N_dot.min(), N_dot.max()))
        fig.canvas.draw_idle()  # redraw the plot




    a_slider.on_changed(update)
    plt.show()

    # sin_ax = plt.axes([0.1, 0.2, 0.8, 0.65])
    # slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])
    #
    # # here we create the slider
    # a_slider = Slider(slider_ax,  # the axes object containing the slider
    #                   'a',  # the name of the slider parameter
    #                   T_array[0],  # minimal value of the parameter
    #                   T_array[-1],  # maximal value of the parameter
    #                   valinit=T_array[0]  # initial value of the parameter
    #                   )
    #
    # # Next we define a function that will be executed each time the value
    # # indicated by the slider changes. The variable of this function will
    # # be assigned the value of the slider.
    # def update(a):
    #
    #     sin_plot.set_ydata(N)  # set new y-coordinates of the plotted points
    #     fig.canvas.draw_idle()  # redraw the plot
    #
    # # the final step is to specify that the slider needs to
    # # execute the above function when its value changes
    # a_slider.on_changed(update)

    plt.show()


def main():
    print('=' * 80)
    print('\tProblem Set 1')
    print('=' * 80)

    problem_1()

    print('=' * 80)
    print('\tEnd of program')
    print('=' * 80)


if __name__ == "__main__":
    main()
