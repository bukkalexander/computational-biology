import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


def problem_1():
    p_1_a()


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

    for i_T in range(n_T):
        plt.plot(t_array, N[i_T, :])
        # plt.show()

    # l, = plt.plot(t_array, N_dot, lw=2)

    # axcolor = 'lightgoldenrodyellow'
    # axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    # axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
    # samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
    # sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
    #
    # def update(val):
    #     amp = samp.val
    #     freq = sfreq.val
    #     l.set_ydata(amp * np.sin(2 * np.pi * freq * t))
    #     fig.canvas.draw_idle()
    #
    # sfreq.on_changed(update)
    # samp.on_changed(update)

    # resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    # button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
    #
    # def reset(event):
    #     sfreq.reset()
    #     samp.reset()
    #
    # button.on_clicked(reset)
    #
    # rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
    # radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
    #
    # def colorfunc(label):
    #     l.set_color(label)
    #     fig.canvas.draw_idle()
    #
    # radio.on_clicked(colorfunc)
    # plt.subplots_adjust(left=0.25, bottom=0.25)

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
