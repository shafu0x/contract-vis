import numpy as np
import matplotlib.pyplot as plt
import os
import sys

if len(sys.argv) != 2:
    print("Usage: python run.py [path to dir]")
    exit(1)
else:
    PATH = sys.argv[1]

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
    for i in range(len(bytecode_list)-2):
        x = int(bytecode_list[i], 16)
        y = int(bytecode_list[i+1], 16)
        z = int(bytecode_list[i+2], 16)
        bytecode_pairs.append((x, y, z))

    bitmap = np.zeros((256, 256, 256), dtype=np.uint8)
    for pair in bytecode_pairs:
        bitmap[pair[0], pair[1], pair[2]] = 255

    bitmaps.append(bitmap)

files = [files[i].split(".")[0] for i in range(6)] # remove extensions

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(6):
    x, y, z = bitmaps[i].nonzero()
    ax.scatter(x, y, z, marker=".", label=files[i])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()

plt.show()
