import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [255, 0, 0]
color2 = [0, 0, 255]

for i, v in enumerate(np.linspace(0, 1, image.shape[0])):
    for j, w in enumerate(np.linspace(0, 1, size)):
        t = (v + w) / 2.0
        r = lerp(color1[0], color2[0], t)
        g = lerp(color1[1], color2[1], t)
        b = lerp(color1[2], color2[2], t)
        image[i, j, :] = [r, g, b]

plt.figure(1)
plt.imshow(image)
plt.show()