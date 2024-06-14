import numpy as np
import matplotlib as plt
from skimage import io
# from einops import rearrange
# np.randompermutation
images = []
for i in range(9):
    images.append(np.load(f"images/car_{i}.npy"))

b = np.sum(images)
print(f"Suma val. pixelilor tuturor img: {b}")

# Calculați suma valorilor pixelilor pentru fiecare imagine în parte.
c = np.sum(images, axis=(1, 2))
print(f"Suma val. px pt fiecare imagine {c}")
# print(np.shape(images))

# Afișați indexul imaginii cu suma maximă.
d = np.argmax(c, axis=0)
print(f"Indexul imaginii cu suma maxima este {d}")


# Calculați imaginea medie și afișati-o
e = np.mean(images, axis=0)
io.imshow(e.astype(np.uint8))
io.show()

#Cu ajutorul funcției np.std(images_array), calculați deviația standard a imaginilor.
f = np.std(images, axis=(1, 2))
print(f"Deviata standard a imaginilor: {f}")




