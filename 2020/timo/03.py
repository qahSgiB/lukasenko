from typing import List


def file_to_array(dir: str) -> List[str]:
    with open(dir, 'r') as f:
        return [line.strip() for line in f]


def count_trees(lines: List[str], x_step: int, y_step: int) -> int:
    x = 0
    count = 0
    for y in range(y_step, len(lines), y_step):
        x += x_step
        if lines[y][x % len(lines[y])] == '#':
            count += 1
    return count


def count_trees_and_multiply(lines: List[str]) -> int:
    return count_trees(lines, 1, 1) * count_trees(lines, 3, 1) * count_trees(lines, 5, 1) * count_trees(lines, 7, 1) * count_trees(lines, 1, 2)


lines = file_to_array('03.txt')
print(count_trees(lines, 3, 1))
print(count_trees_and_multiply(lines))
