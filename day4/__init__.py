from .day4 import day4_part1, day4_part2
from parsers import read_file

inputs = read_file("day4/data.txt")


def run_day4():
    result1 = sum([day4_part1(item) for item in inputs])
    print(f"day4_part1 >>>>>>>>>>>>>>>>>>>> {result1}")

    result2 = sum([day4_part2(item) for item in inputs])
    print(f"day4_part2 >>>>>>>>>>>>>>>>>>>> {result2}")



