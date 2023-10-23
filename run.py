PATH = "/Users/shafu/contract-vis/examples/dnft.bytecode"

with open(PATH, "r") as f:
    bytecode = f.read()

bytecode = bytecode[2:]

bytecode_list = [bytecode[i:i+2] for i in range(0, len(bytecode), 2)]
bytecode_list = bytecode_list[:-1]

bytecode_pairs = []
for i in range(len(bytecode_list)-1):
    bytecode_pairs.append((int(bytecode_list[i], 16), int(bytecode_list[i+1], 16)))

print("Bytecode: ", bytecode)
print("Bytecode list: ", bytecode_list)
print("Bytecode pairs: ", bytecode_pairs)

