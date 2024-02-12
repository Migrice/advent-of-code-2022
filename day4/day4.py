

def day4_part1(pair: str) -> int:
    pair_list = pair.split(",")
    data_list = []
    data_list.append(int(pair_list[0].split("-")[0]))
    data_list.append(int(pair_list[0].split("-")[1]))
    data_list.append(int(pair_list[1].split("-")[0]))
    data_list.append(int(pair_list[1].split("-")[1]))

    if data_list[0] < data_list[2] and data_list[1] > data_list[3]:
        return 1

    if data_list[0] > data_list[2] and data_list[1] == data_list[3]:
        return 1

    if data_list[0] > data_list[2] and data_list[1] < data_list[3]:
        return 1

    if data_list[0] == data_list[2] or data_list[1] == data_list[3]:
        return 1

    return 0


def day4_part2(pair: str) -> int:
    pair_list = pair.split(",")
    A = []
    B = []
    A.append(int(pair_list[0].split("-")[0]))
    A.append(int(pair_list[0].split("-")[1]))
    B.append(int(pair_list[1].split("-")[0]))
    B.append(int(pair_list[1].split("-")[1]))

    if A[0] < B[0] and A[1] >= B[0]:
        return 1

    if B[0] < A[0] and B[1] >= A[0]:
        return 1

    if A[0] == B[0]:
        return 1

    if A[1] == B[1]:
        return 1

    return 0


o = day4_part2("28-39,8-41")
print(o)
