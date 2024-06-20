
## BROKEN

import numpy as np
import matplotlib.pyplot as plt


hex_colors = ['004daaff', 'e76200ff', '00a900ff', 'bd0020ff', 'ffae00ff', '74007aff', '6b6b6bff']

def hex_to_rgb(hex_color):  
    # Convert hex to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    a = int(hex_color[6:8], 16)

    # Return RGBA array
    return [r, g, b, a]  # Assuming alpha is 255 (fully opaque)

# Convert each hex color to RGBA array
Cs = np.array([hex_to_rgb(color) for color in hex_colors], dtype=int)
Cs = Cs/255

C = Cs[[0, 2]]

x_N = 300

x = np.linspace(0, 2, x_N)

H = np.zeros((x_N, 2, 2))
H[:, 0, 0] = 1 + 0.5 * x
H[:, 1, 1] = 3 - 1.5 * x

w0 = np.zeros((x_N, 2), dtype=float)
v0 = np.zeros((x_N, 2, 2), dtype=complex)
for n in range(x_N):
    w0[n], v0[n] = np.linalg.eigh(H[n])

w0, v0 = sort_eigensystem(w0, v0)

H[:, 0, 1] = 0.05
H[:, 1, 0] = 0.05

w = np.zeros((x_N, 2), dtype=float)
v = np.zeros((x_N, 2, 2), dtype=complex)
for n in range(x_N):
    w[n], v[n] = np.linalg.eigh(H[n])

c0 = matplotlib_default_colors[:2]

fig, ax = plt.subplots(figsize=(3.375, 3.375))
lc = plot_spectrum(x, v0=v0, w=w, v=v, c0=C[:2])
ax.add_collection(lc)
ax.plot(x, w0[:, 0], "--", color=C[0], alpha=0.3)
ax.plot(x, w0[:, 1], "--", color=C[1], alpha=0.3)

ax.set_xlim(0, 2)
ax.set_ylim(0, 3)


fig.tight_layout()
fig.savefig("logo.svg") 