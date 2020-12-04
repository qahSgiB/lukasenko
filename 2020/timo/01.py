from typing import List, Optional


def file_to_array(dir: str) -> List[int]:
    f = open(dir, 'r')
    items: List[int] = []
    for line in f:
        items.append(int(line))
    f.close()
    return items


def puzzle1(items: List[int]) -> Optional[int]:
    for x in range(len(items)):
        for y in range(x + 1, len(items)):
            if items[x] + items[y] == 2020:
                return items[x] * items[y]
    return None


def puzzle2(items: List[int]) -> Optional[int]:
    for x in range(len(items)):
        for y in range(x + 1, len(items)):
            for z in range(y + 1, len(items)):
                if items[x] + items[y] + items[z] == 2020:
                    return items[x] * items[y] * items[z]
    return None


print(puzzle1(file_to_array('01.txt')))
print(puzzle2(file_to_array('01.txt')))
