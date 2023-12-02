import re
from functools import reduce
from typing import List, Dict


with open('Day1/input.txt') as file:
    lines: List[str]  = file.read().strip().split('\n')

def get_calibration_code(lines: List[str]) -> int:
    return sum(map(lambda x: int(x[0] + x[-1]), [re.findall("\d", i) for i in lines]))

def word2digit(lines: List[str]) -> List[str]:
    replacements: Dict[str, str] = \
        {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 
         'seven': 's7n', 'eight': 'e8n', 'nine': 'n9e'}
        #To avoid problems like 'oneight'

    return [reduce(lambda x, item: x.replace(item[0], item[1]), replacements.items(), line) \
             for line in lines]

def main():
    print('Part 1: {}'.format(get_calibration_code(lines)))
    print('Part 2: {}'.format(get_calibration_code(word2digit(lines))))

if __name__ == '__main__':
    main()
