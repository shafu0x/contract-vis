import numpy as np

# get all files in directory
import os
files = os.listdir("/Users/shafu/contract-vis/examples")

bitmaps = []

for file in files:
    path = "/Users/shafu/contract-vis/examples/" + file

    with open(path, "r") as f:
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

    bitmaps.append(bitmap)

# visualize the bitmaps in one plot
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 3)

bitmaps = [bitmaps[i] for i in range(6)]
files = [files[i].split(".")[0] for i in range(6)]

for i in range(2):
    for j in range(3):
        index = i * 3 + j
        axes[i, j].imshow(bitmaps[index], cmap="gray")
        axes[i, j].set_title(files[index])

plt.show()
