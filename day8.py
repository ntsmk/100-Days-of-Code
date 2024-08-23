def calculate_love_score(name1, name2):
    name = name1 + name2
    count1 = 0
    for i in name.lower():
        if "t" in i:
            count1 += 1
        elif "r" in i:
            count1 += 1
        elif "u" in i:
            count1 += 1
        elif "e" in i:
            count1 += 1

    count2 = 0
    for i in name.lower():
        if "l" in i:
            count2 += 1
        elif "o" in i:
            count2 += 1
        elif "v" in i:
            count2 += 1
        elif "e" in i:
            count2 += 1

    print(str(count1) + str(count2))


calculate_love_score("Angela Yu", "Jack Bauer")