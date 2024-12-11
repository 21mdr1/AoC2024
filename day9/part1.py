from utils import print_result, input_file, test


def parse_diskmap(input):
    diskmap = []
    id = 0

    for i, length in enumerate(input):
        if i % 2 == 0:
            diskmap.append([id, int(length)])
            id = (id + 1) % 10
        else:
            diskmap.append([-1, int(length)])

    return diskmap

def strip_end(diskmap):
    while True:
        if diskmap[-1][0] == -1:
            diskmap.pop()
        else:
            return diskmap
        

def move_last(diskmap):
    diskmap = strip_end(diskmap)
    
    id, length = diskmap.pop()

    for i, block in enumerate(diskmap):
        if block[0] == -1:
            if block[1] > length:
                block[1] -= length
                diskmap.insert(i, [id, length])
                length = 0

            else:
                block[0] = id
                length -= block[1]

        if length == 0:
            return diskmap
    
    diskmap.append([id, length])
    return diskmap


def can_move(diskmap):
    diskmap = strip_end(diskmap)
    
    for entry in diskmap:
        if entry[0] == -1:
            return True
    
    return False

def checksum(diskmap):
    checksum = 0
    position = 0

    for block in diskmap:
        id, length = block

        if id == -1:
            position += length
            continue

        for _ in range(length):
            checksum += (id * position)
            position += 1

    return checksum

@print_result
def solve(input_file: str) -> int:
    input = open(input_file, "r").read().strip("\n")
    diskmap = parse_diskmap(input)

    while can_move(diskmap):
        diskmap = move_last(diskmap)

    return checksum(diskmap)


test(solve, 9, 1928)
solve(input_file(9))
# 5548088938 is too low