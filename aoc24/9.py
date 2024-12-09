from utils import *

INPUT_FILE = "./9.in"
SAMPLE_FILE = "./9.sample"

input = [int(x) for x in list(read_to_string(SAMPLE_FILE).strip())]

# print(input)

free_spaces = input[1::2]
file_blocks = [(block, i) for block, i in enumerate(input[::2])]

# print(free_spaces)
# print(file_blocks)
# print(total_file_blocks)

defragmented_blocks = []
defragmented_filesystem = []
defragmented_blocks.append(file_blocks[0])
defragmented_filesystem.append(file_blocks[0])
file_blocks_position = 1

for id, nr_file_blocks in reversed(file_blocks):
    if (id, nr_file_blocks) in defragmented_blocks:
        # print(f"File {(id, nr_file_blocks)} already defragmented")
        continue
    defragmented_blocks.append((id, nr_file_blocks))
    # print(f"Check file {id} with {nr_file_blocks} blocks")
    file_blocks_defragmented = 0
    while file_blocks_defragmented < nr_file_blocks:
        remaining_blocks = nr_file_blocks - file_blocks_defragmented
        # if len(defragmented_blocks) == len(file_blocks):
        #     defragmented_filesystem.append((id, nr_file_blocks - file_blocks_defragmented))
        #     break
        if remaining_blocks > free_spaces[0]:
            # print(f"File {id} with {nr_file_blocks - file_blocks_defragmented} remaining blocks is too big for free space {free_spaces[0]}")
            spaces = free_spaces.pop(0)
            defragmented_filesystem.append((id, spaces))
            # print(f"Added {spaces} blocks for file {id}")
            file_blocks_defragmented += spaces
            next_file_block = file_blocks[file_blocks_position]
            if next_file_block not in defragmented_blocks:
                defragmented_filesystem.append(next_file_block)
                # print(f"Added {next_file_block} to defragmented filesystem")
                defragmented_blocks.append(next_file_block)
            file_blocks_position += 1
        else:
            # print(f"File {id} with {nr_file_blocks - file_blocks_defragmented} remaining blocks fits in free space {free_spaces[0]}")
            spaces = free_spaces.pop(0)
            defragmented_filesystem.append((id, remaining_blocks))
            file_blocks_defragmented += remaining_blocks
            # print(f"Added {file_blocks_defragmented} blocks for file {id}")
            if spaces - remaining_blocks > 0:
                free_spaces.insert(0, spaces - remaining_blocks)
            else:
                next_file_block = file_blocks[file_blocks_position]
                if next_file_block not in defragmented_blocks:
                    defragmented_filesystem.append(next_file_block)
                    # print(f"Added {next_file_block} to defragmented filesystem")
                    defragmented_blocks.append(next_file_block)
                file_blocks_position += 1
        # print(f"Free spaces: {free_spaces}")
    # print(f"File {id} defragmented")
    # print(f"Defragmented filesystem: {defragmented_filesystem}")
    # print("---")

sum = 0
index = 0
for id, nr_file_blocks in defragmented_filesystem:
    for _ in range(nr_file_blocks):
        sum += index * id
        index += 1
print(sum)