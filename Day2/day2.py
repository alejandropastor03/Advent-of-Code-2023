import re
from functools import reduce
from typing import List, Tuple


with open('Day2/input.txt') as file:
    lines: List[str]  = file.read().strip().split('\n')

def get_sum_valid_games(lines: List[str]) -> int:
    pattern: str = '1[3-9] red|[2-9]\d red|1[4-9] green|[2-9]\d green|1[5-9] blue|[2-9]\d blue'
    valid_games: List[bool] = list(map(lambda x: True if not x else False, 
                                       [re.findall(pattern, i) for i in lines]))
    return sum(index+1 for index, value in enumerate(valid_games) if value)

def get_sum_power(lines:List[str]) -> int:

    def get_min(list_tuples: List[Tuple[str, str]]) -> List[int]:
        min_colors: List[int] = [0, 0, 0] #0 red, 1 blue, 2 green
        for tuple in list_tuples:
            if tuple[1] == 'red' and min_colors[0] < int(tuple[0]):
                min_colors[0] = int(tuple[0])
            if tuple[1] == 'blue' and min_colors[1] < int(tuple[0]):
                min_colors[1] = int(tuple[0])
            if tuple[1] == 'green' and min_colors[2] < int(tuple[0]):
                min_colors[2] = int(tuple[0])
        return min_colors

    pattern: str = '\d+ red|\d+ green|\d+ blue'
    min_per_game: List[List[int]] = list(map(lambda x: get_min([tuple(i.split()) for i in x]),
                                    [re.findall(pattern, i) for i in lines]))
    return sum([reduce(lambda x, y: x * y, mins) for mins in min_per_game])

def main():
    print('Part 1: {}'.format(get_sum_valid_games(lines)))
    print('Part 2: {}'.format(get_sum_power(lines)))

if __name__ == '__main__':
    main()
