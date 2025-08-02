import numpy as np
import matplotlib.pyplot as plt

# Parameters for the image
width, height = 800, 800
max_iter = 100  # Iterations for divergence

# Define the range in the complex plane
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

# Generate the real and imaginary axis
real = np.linspace(xmin, xmax, width)
imag = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(real, imag)
C = X + 1j * Y

# Initialize the Mandelbrot array
Z = np.zeros_like(C)
divergence_time = np.zeros(C.shape, dtype=int)

# Mandelbrot iteration
for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask] ** 2 + C[mask]
    divergence_time[mask & (np.abs(Z) > 2)] = i

# Plot the result
plt.figure(figsize=(8, 8))
plt.imshow(divergence_time, cmap='hot', extent=[xmin, xmax, ymin, ymax])
plt.title("Mandelbrot Set")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.colorbar(label='Divergence Time')
plt.show()
