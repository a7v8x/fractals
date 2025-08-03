import numpy as np
import matplotlib.pyplot as plt

# Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Time settings
dt = 0.01
steps = 10000

# Arrays to store the solution
xs = np.empty(steps)
ys = np.empty(steps)
zs = np.empty(steps)

# Initial values
xs[0], ys[0], zs[0] = (1.0, 1.0, 1.0)

# Euler integration of Lorenz equations
for i in range(1, steps):
    dx = sigma * (ys[i-1] - xs[i-1])
    dy = xs[i-1] * (rho - zs[i-1]) - ys[i-1]
    dz = xs[i-1] * ys[i-1] - beta * zs[i-1]
    
    xs[i] = xs[i-1] + dx * dt
    ys[i] = ys[i-1] + dy * dt
    zs[i] = zs[i-1] + dz * dt

# Plotting the Lorenz attractor
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, lw=0.5)
ax.set_title("Lorenz Attractor")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.show()
