import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


def problem_1():
    p_1_a()


def p_1_a():
    # fig, ax = plt.subplots()
    #
    # t_start = 0.0
    # t_step_size = 0.001
    # t_end = 1.0
    # t = np.arange(t_start, t_end, t_step_size)
    #
    # r = 1.0
    # K = 10
    # A = 5
    #
    # N_0 = 50
    # N_delay_0 = 40
    #
    #
    # N = N_0
    # N_delay = N_delay_0
    #
    # def N_dot(t):
    #     for i in range(len(t)):
    #         r*N * (1 - N_delay/K) * (N/A - 1)
    #
    # l, = plt.plot(t, N_dot, lw=2)

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
