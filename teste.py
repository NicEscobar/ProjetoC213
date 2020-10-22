from control import *
from control.matlab import c2d
import matplotlib.pyplot as plt

g = tf(1, [1, 1, 1])

gz = c2d(g, 0.1)

t = np.arange(0, 16, 0.1)

t1, y = step_response(gz, t)

plt.step(t, y)
plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.show()
