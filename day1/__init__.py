from .day1 import day1_part1, day1_part_2
from parsers import read_file


inputs = read_file("day1/data.txt")

def run_day1():
    result1 = day1_part1(inputs)
    print(f"day1_part1 >>>>>>>>>>> {result1}")

    result2 = day1_part_2(inputs=inputs)
    print(f"day1_part2 >>>>>>>>>>>> {result2} ")
    