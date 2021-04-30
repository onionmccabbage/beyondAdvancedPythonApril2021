import numpy as np
np.random.seed(12345)
# np.set_printoptions(precision=4)
import matplotlib.pyplot as plt # convention

my_arr = np.arange(1000000) #
print((my_arr))

points = np.arange(-5, 5, 0.001) # 1000 equally spaced points
points
xs, ys = np.meshgrid(points, points)
xs
# %time
z = np.sqrt(xs**2 + ys**2) # pythagorus
print(z)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()

plt.draw()
plt.savefig('myplot.png')

