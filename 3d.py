import numpy as np
import matplotlib.pyplot as plt
import os
import sys

if len(sys.argv) != 2:
    print("Usage: python run.py [path to file]")
    exit(1)
else:
    file = sys.argv[1]

with open(file, "r") as f:
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


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = bitmap.nonzero()[0]
y = bitmap.nonzero()[1]
z = bitmap.nonzero()[2]
ax.scatter(x, y, z, marker=".", label=file.split("/")[-1].split(".")[0])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()

plt.show()
