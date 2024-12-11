from utils import print_result, input_file, test, use_input_file

def parse_diskmap(input):
    diskmap = []
    id = 0

    for i, length in enumerate(input):
        if i % 2 == 0:
            diskmap.append([id, int(length)])
            id += 1
        else:
            if length != "0": diskmap.append([-1, int(length)])

    return diskmap

def is_space(block):
    return block[0] == -1

def move_last_block(diskmap):
    id, length = diskmap.pop()

    for i, block in enumerate(diskmap):
        if is_space(block) and block[1] >= length:
            block[1] -= length
            diskmap.insert(i, [id, length])
            diskmap.append([-1, length])
            return diskmap, True
    
    diskmap.append([id, length])
    return diskmap, False

def checksum(diskmap):
    checksum = 0
    position = 0

    for block in diskmap:
        id, length = block

        if id > 0:
            checksum += (length * (2 * position + length - 1) * id // 2)
        
        position += length

    return checksum

@print_result
@use_input_file
def solve(input: str) -> int:
    diskmap = parse_diskmap(input.strip("\n"))
    compacted_diskmap = []
    
    while len(diskmap) > 0:
        if is_space(diskmap[-1]):
            compacted_diskmap.append(diskmap.pop())
        else:
            diskmap, could_be_moved = move_last_block(diskmap)
            if not could_be_moved:
                compacted_diskmap.append(diskmap.pop())

    return checksum(list(reversed(compacted_diskmap)))

test(solve, input_file(9, True), 2858)
solve(input_file(9))
