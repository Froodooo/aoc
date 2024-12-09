from utils import *

INPUT_FILE = "./9.in"
SAMPLE_FILE = "./9.sample"

input = [int(x) for x in list(read_to_string(INPUT_FILE).strip())]

free_spaces = input[1::2]
# print(free_spaces)
file_blocks = [(block, i) for block, i in enumerate(input[::2])]
# print(file_blocks)

file_blocks_copy = [x for x in file_blocks]
seen = []
seen.append(file_blocks_copy[0][0])

for file_block_idx, (id, nr_file_blocks) in enumerate(reversed(file_blocks_copy)):
    if id in seen:
        continue
    seen.append(id)
    # print(f"Check file {id} with {nr_file_blocks} blocks")
    free_space_idx = next((i for i in range(len(free_spaces)) if free_spaces[i] >= nr_file_blocks and i <= len(file_blocks) - file_block_idx - 1), None)
    if free_space_idx is not None:
        # print(f"Found free space at index {free_space_idx} with {free_spaces[free_space_idx]} blocks")
        # del(free_spaces[len(file_blocks) - file_block_idx - 2])
        free_spaces.insert(free_space_idx + 1, free_spaces[free_space_idx] - nr_file_blocks)
        free_spaces[free_space_idx] = 0
        file_blocks_index = file_blocks.index((id, nr_file_blocks))
        file_blocks.insert(free_space_idx + 1, file_blocks.pop(file_blocks_index))
        # print(f"File blocks after defragmentation: {file_blocks}")
        # if file_block_idx == 0:
        # print(f"File blocks index: {file_blocks_index}")
        # free_spaces[file_blocks_index - 1] = free_spaces[file_blocks_index - 1] + nr_file_blocks
        # else:
        if file_blocks_index == len(file_blocks) - 1:
            free_spaces.pop(file_blocks_index)
            # free_spaces[file_blocks_index] = free_spaces[file_blocks_index - 2] + nr_file_blocks
        else:
            free_spaces[file_blocks_index] = free_spaces[file_blocks_index - 1] + nr_file_blocks + free_spaces.pop(file_blocks_index - 1)
        # print(f"Free space after defragmentation: {free_spaces}")
    
sum = 0
    
print(len(file_blocks))
print(len(free_spaces))
    
index = 0
for i, (id, nr_file_blocks) in enumerate(file_blocks):
    for j in range(nr_file_blocks):
        sum += (index + j) * id
    index += nr_file_blocks + free_spaces[i] if i < len(free_spaces) else 0
print(sum)

# 7107402132147 - too high