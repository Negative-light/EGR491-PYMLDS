import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim
from matplotlib.animation import FuncAnimation
fig = plt.figure()
data_x, data_y = [], []

plt.xlim(-10, 10)
plt.ylim(-10, 10)


def anim_func(i):
    for j in range(0, 10):
        data_x.append(np.random.randint(-10, 10))
        data_y.append(np.random.randint(-10, 10))

    if(i % 10 == 0):
        print(i)

    plt.hexbin(data_x, data_y, cmap='Reds', gridsize=2*((i//10)+1))


ani = FuncAnimation(fig, anim_func, interval=1, save_count=300, repeat=False)
f = r"./test_ani.gif"
print(f)

writergif = anim.PillowWriter(fps=30)
ani.save(f, writer=writergif)
print("saved")
