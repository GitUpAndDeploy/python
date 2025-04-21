def calculate_love_score(name1, name2):
    name1 = list(name1)
    name2 = list(name2)
    name_1_score = 0
    name_2_score = 0
    for letter in (name1+name2):
        if "t" == letter:
            name_1_score += 1
        elif "r" == letter:
            name_1_score += 1
        elif "u" == letter:
            name_1_score += 1
        elif "e" == letter:
            name_1_score += 1
    for letter in (name1+name2):
        if "l" == letter:
            name_2_score += 1
        elif "o" == letter:
            name_2_score += 1
        elif "v" == letter:
            name_2_score += 1
        elif "e" == letter:
            name_2_score += 1
    print(str(name_1_score) + str(name_2_score))

calculate_love_score("Kanye West", "Kim Kardashian")
