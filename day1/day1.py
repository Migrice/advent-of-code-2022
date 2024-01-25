

def day1_part1(inputs: list[str]):

    somme = []
    value = 0

    for i in range(len(inputs)):
        if inputs[i] != "" :
            value += int(inputs[i])
            if i  == (len(inputs)-1):
                somme.append(value)
        else:
            somme.append(value)
            value = 0
        
    return max(somme)

def day1_part_2(inputs: list[str]):

    somme = []
    value = 0

    for i in range(len(inputs)):
        if inputs[i] != "" :
            value += int(inputs[i])
            if i  == (len(inputs)-1):
                somme.append(value)
        else:
            somme.append(value)
            value = 0
    
    new_somme = sorted(somme, reverse=True)
    max_sum = sum(new_somme[0:3])
    return max_sum