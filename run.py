import numpy as np
import matplotlib.pyplot as plt
import os

PATH = "/Users/shafu/contract-vis/examples/"
files = os.listdir(PATH)

bitmaps = []

for file in files:
    path = PATH + file

    with open(path, "r") as f:
        bytecode = f.read()

    if bytecode[:2] == "0x":
        bytecode = bytecode[2:] 

    bytecode_list = [bytecode[i:i+2] for i in range(0, len(bytecode), 2)]
    bytecode_list = bytecode_list[:-1] # remove \n

    bytecode_pairs = []
    for i in range(len(bytecode_list)-1):
        x = int(bytecode_list[i], 16)
        y = int(bytecode_list[i+1], 16)
        bytecode_pairs.append((x, y))

    bitmap = np.zeros((256, 256), dtype=np.uint8)
    for pair in bytecode_pairs:
        bitmap[pair[0], pair[1]] = 255

    bitmaps.append(bitmap)

fig, axes = plt.subplots(2, 3)

files = [files[i].split(".")[0] for i in range(6)] # remove extensions

for i in range(2):
    for j in range(3):
        index = i * 3 + j
        axes[i, j].imshow(bitmaps[index], cmap="gray")
        axes[i, j].set_title(files[index])

plt.show()
