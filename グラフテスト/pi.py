import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
x = np.arange(-2 * pi, 2 * pi, 0.1)
y = np.tan(x)
plt.ylim([-5, 5])  # tanはyの値が無限大になるので表示範囲を適当に制限
plt.xticks(
    [-2 * pi, -pi, 0, pi, 2 * pi],
    ['-2π', '-π', '0', 'π', '2π']
)
plt.gca().set_aspect('equal')
plt.grid()
plt.xlabel('x')
plt.ylabel('y',  rotation=0)
plt.plot(x, y)
plt.show()
