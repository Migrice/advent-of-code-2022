def day2_part1(input):
    match_values = {"A": "X", "B": "Y", "C": "Z"}

    points = {"X": 1, "Y": 2, "Z": 3}

    word = input.split(" ")

    word[0] = match_values[word[0]]

    score = points[word[1]]

    if word[0] == word[1]:
        score += 3

    elif (
        (word[0] == "X" and word[1] == "Y")
        or (word[0] == "Y" and word[1] == "Z")
        or (word[0] == "Z" and word[1] == "X")
    ):
        score += 6

    return score


def day2_part2(pair):
    points = {"A": 1, "B": 2, "C": 3}

    op = pair.split(" ")[0]
    ans = pair.split(" ")[1]

    if ans == "Y":
        score = 3 + points[op]
    elif ans == "X" and op == "A":
        score = points["C"]
    elif ans == "X" and op == "B":
        score = points["A"]
    elif ans == "X" and op == "C":
        score = points["B"]
    elif ans == "Z" and op == "A":
        score = points["B"] + 6
    elif ans == "Z" and op == "B":
        score = points["C"] + 6
    elif ans == "Z" and op == "C":
        score = points["A"] + 6

    return score
