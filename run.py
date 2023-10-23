import numpy as np

PATH = "/Users/shafu/contract-vis/examples/dnft.bytecode"

with open(PATH, "r") as f:
    bytecode = f.read()

bytecode = bytecode[2:]

bytecode_list = [bytecode[i:i+2] for i in range(0, len(bytecode), 2)]
bytecode_list = bytecode_list[:-1]

bytecode_pairs = []
for i in range(len(bytecode_list)-1):
    bytecode_pairs.append((int(bytecode_list[i], 16), int(bytecode_list[i+1], 16)))

bitmap = np.zeros((256, 256), dtype=np.uint8)
for pair in bytecode_pairs:
    bitmap[pair[0], pair[1]] = 255

print(bitmap)

# visualize the bitmap
import matplotlib.pyplot as plt
plt.imshow(bitmap, cmap='gray')
plt.show()
