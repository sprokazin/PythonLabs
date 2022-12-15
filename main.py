import numpy as np
from scipy import special
import matplotlib.pylab as plt
from numpy import sin,pi
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import collections

#1
def task1():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    n_max = 7
    x = np.linspace(-1, 1)
    y = np.array([special.lpn(n_max, xi)[0]  for xi in x]).T
    for n, yn in enumerate(y):
        ax.plot(x, yn, label = 'n = ' + str(n), linewidth=2)
    ax.legend(fontsize=14, loc=4)
    ax.set_xlabel('t', fontsize=14)
    ax.set_ylabel('$P_n (t)$', fontsize=14)
    ax.set_xlim(-1, 1)
    ax.grid()
    ax.set_title('Полиномы Лежандра')
    plt.show()

#2
def task2():
    m=[[3,2],[3,4],[5,4],[5,6]]
    plt.figure(1)
    for i in m:
             a=i[0]
             b=i[1]
             d=0.5*pi
             x=[sin(a*t+d) for t in np.arange(0.,2*pi,0.01)]
             y=[sin(b*t) for t in np.arange(0.,2*pi,0.01)]
             if m.index(i)==0:
                      plt.subplot(221)
                      plt.plot(x, y, 'k')
                      plt.grid(True)
             elif m.index(i)==1:
                      plt.subplot(222)
                      plt.plot(x, y, 'g')
                      plt.grid(True)
             elif m.index(i)==2:
                      plt.subplot(223)
                      plt.plot(x, y, 'b')
                      plt.grid(True)
             else:
                      plt.subplot(224)
                      plt.plot(x, y, 'r')
                      plt.grid(True )
    plt.show()

#3
def task3():
    fig = plt.figure()
    ax = plt.subplot()
    t = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    b = 5
    def animate(i):
        a = b * (0.01 * i)
        x = np.sin(a * t)
        y = np.sin(b * t)
        ax.clear()
        plt.plot(x, y, 'b')
        return fig
    anim = FuncAnimation(fig, animate, frames=100, interval=20, blit=False)
    plt.show()


#4
def task4():
    def initialWave(a1, f1, a2, f2):
        x = np.arange(0.0, 2, 0.001)
        y1 = a1 * np.sin(2 * np.pi * f1 * x)
        y2 = a2 * np.sin(2 * np.pi * f2 * x)
        y = y1 + y2
        return x, y1, y2, y

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.4)
    x, y1, y2, y = initialWave(5, 3, 5, 4)
    plt.subplot(131)
    l1, = plt.plot(x, y1, lw=2, color='red')
    plt.subplot(132)
    l2, = plt.plot(x, y2, lw=2, color='blue')
    plt.subplot(133)
    l3, = plt.plot(x, y, lw=2, color='green')

    axamp1 = plt.axes([0.25, 0.1, 0.65, 0.03])
    axfreq1 = plt.axes([0.25, 0.15, 0.65, 0.03])
    axamp2 = plt.axes([0.25, 0.2, 0.65, 0.03])
    axfreq2 = plt.axes([0.25, 0.25, 0.65, 0.03])

    def update(var):
        a1 = amp1.val
        f1 = freq1.val
        a2 = amp2.val
        f2 = freq2.val
        x, y1, y2, y = initialWave(a1, f1, a2, f2)
        print(y1)
        l1.set_ydata(y1)
        l2.set_ydata(y2)
        l3.set_ydata(y)
        fig.canvas.draw_idle()

    amp1 = Slider(axamp1, 'Amp1', 0.1, 10.0, valinit=5)
    freq1 = Slider(axfreq1, 'Freq1', 0.1, 30.0, valinit=3)
    amp2 = Slider(axamp2, 'Amp2', 0.1, 10.0, valinit=5)
    freq2 = Slider(axfreq2, 'Freq2', 0.1, 30.0, valinit=2)

    amp1.on_changed(update)
    freq1.on_changed(update)
    amp2.on_changed(update)
    freq2.on_changed(update)

    plt.show()


#5
def MSE(m, b, points):
    total = 0
    for i in range(0, len(points)):
        total += (points[i].y - (m * points[i].x + b)) ** 2
    return total / float(len(points))


def task5():
    x = np.arange(-7.0, 7.0, 0.05)
    Point = collections.namedtuple('Point', ['x', 'y'])

    val1, val2 = 3, 2
    noise = np.random.random(x.size)
    points = [Point(xp, val1 * xp + val2 + err) for xp, err in zip(x, noise)]

    fig = plt.figure()
    ax = fig.add_subplot(121, projection='3d')

    s1 = np.linspace(2.0, 4.0, 10)
    s2 = np.linspace(-10, 10, 10)

    X, Y = np.meshgrid(s1, s2)
    s3 = np.array([MSE(mp, bp, points)
                   for mp, bp in zip(np.ravel(X), np.ravel(Y))])
    Z = s3.reshape(X.shape)

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='b', alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('MSE')

    Zlog = np.log(Z)

    ax = fig.add_subplot(122, projection='3d')
    ax.plot_surface(X, Y, Zlog, rstride=1, cstride=1, color='b', alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('MSE')

    plt.show()

if __name__ == '__main__':
    #task1()
    #task2()
    #task3()
    #task4()
    task5()