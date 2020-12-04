from typing import List
from typing import NamedTuple


class CodeParts(NamedTuple):
    min: int
    max: int
    letter: str
    password: str


def decompose(code: str) -> CodeParts:
    code_parts = code.split(' ')
    range_start, range_end = code_parts[0].split('-')
    letter = code_parts[1].strip(':')
    code = code_parts[2]
    return CodeParts(int(range_start), int(range_end), letter, code)


def file_to_array(dir: str) -> List[CodeParts]:
    with open(dir, 'r') as f:
        return [decompose(line.strip()) for line in f]


def is_validA(code_parts: CodeParts) -> bool:
    valid_letters = list(filter(lambda letter: letter == code_parts.letter, code_parts.password))
    return code_parts.min <= len(valid_letters) <= code_parts.max


def is_validB(code_parts: CodeParts) -> bool:
    return (code_parts.password[code_parts.min - 1] == code_parts.letter) != \
            (code_parts.password[code_parts.max - 1] == code_parts.letter)


print(len(list(filter(is_validA, file_to_array('02.txt')))))
print(len(list(filter(is_validB, file_to_array('02.txt')))))
