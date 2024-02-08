from .day3 import day3_part1, day3_part2
from parsers import read_file

inputs = read_file("day3/data.txt")


def run_day3():
    result1 = sum([day3_part1(item) for item in inputs])
    print(f"day3_part1 >>>>>>>>>>>>>>>>>>>> {result1}")

    sous_listes_triplets = []
    for i in range (0, len(inputs), 3):
        sous_liste = inputs[i:i+3]
        sous_listes_triplets.append(sous_liste)

    result2 = sum([day3_part2(triplet) for triplet in sous_listes_triplets])
    print(f"day3_part2 >>>>>>>>>>>>>>>>>>>> {result2}")



