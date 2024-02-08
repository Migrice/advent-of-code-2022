import string

lower_alphabet = list(string.ascii_lowercase)
lower_priorities = [i + 1 for i in range(26)]

letter_priority_lower_match = dict(zip(lower_alphabet, lower_priorities))


def day3_part1(item: str):
    long = len(item)
    middle = int(long / 2)
    part1 = item[0:middle]
    part2 = item[middle:long]

    for letter in list(part1):
        if letter in list(part2):
            true_letter = letter
            break

    if true_letter.islower():
        priority = letter_priority_lower_match[true_letter]
    else:
        letter_to_lower = true_letter.lower()
        priority = letter_priority_lower_match[letter_to_lower] + 26

    return priority



def day3_part2(triplets: list[str])-> str:
    for letter in list(triplets[0]):
        if letter in list(triplets[1]) and letter in list(triplets[2]):
            true_letter = letter
            break
    if true_letter.islower():
        priority = letter_priority_lower_match[true_letter]
    else:
        letter_to_lower = true_letter.lower()
        priority = letter_priority_lower_match[letter_to_lower] + 26
    return priority
