from typing import List, Callable


def file_to_array(dir: str) -> List[List[str]]:
    data: List[str] = []
    list_of_data: List[List[str]] = []
    with open(dir, 'r') as f:
        for line in f:
            if line.strip() == '':
                list_of_data.append(data)
                data = []
            else:
                data += (line.strip().split(' '))
        list_of_data.append(data)
    return list_of_data


def validateA(data: List[str]) -> bool:
    if len(data) == 7:
        for key in data:
            if key[:3] == 'cid':
                return False
        return True
    if len(data) == 8:
        return True
    return False


def validateB(data: List[str]) -> bool:
    if not validateA(data):
        return False
    else:
        for field in data:
            key = field[:3]
            value = field[4:]
            if key == 'byr':
                if not (1920 <= int(value) <= 2002):
                    return False
            if key == 'iyr':
                if not (2002 <= int(value) <= 2020):
                    return False
            if key == 'eyr':
                if not (2020 <= int(value) <= 2030):
                    return False
            if key == 'hgt':
                if field[-2:] == 'cm':
                    if not (150 <= int(value.strip('cm')) <= 193):
                        return False
                elif field[-2:] == 'in':
                    if not (59 <= int(value.strip('in')) <= 76):
                        return False
                else:
                    return False
            if key == 'hcl':
                if not (field[4] == '#' and len(field[5:]) == 6):
                    return False
                for symbol in field[5:]:
                    if not symbol.isdecimal():
                        if 97 > ord(symbol) > 102:
                            return False
            if key == 'ecl':
                if not (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                    return False
            if key == 'pid':
                if len(value) != 9:
                    return False
        return True


def count_valid(list_of_data: List[List[str]], validate: Callable[[List[str]], bool]) -> int:
    count = 0
    for data in list_of_data:
        if validate(data):
            count += 1
    return count


list_of_data = file_to_array('04.txt')
print(count_valid(list_of_data, validateA))
print(count_valid(list_of_data, validateB))
