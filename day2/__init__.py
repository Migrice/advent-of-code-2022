from parsers import read_file
from .day2 import day2_part1, day2_part2

inputs = read_file("day2/data.txt")


def run_day2():
    result1 = sum([day2_part1(pair) for pair in inputs])
    print(f"day2_part1 >>>>>>>>>>>>>>>  {result1}")

    result2 = sum([day2_part2(pair) for pair in inputs])
    print(f"day2_part2 >>>>>>>>>>>>>>>  {result2}")
