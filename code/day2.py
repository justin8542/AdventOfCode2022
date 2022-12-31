with open('../inputs/day2.txt', 'r') as f:
    totalPoints = 0
    bonus = {'X':0,'Y':3,'Z':6}
    for line in f:
        line = line.strip()
        opp = line[0]
        us = line[2]
        #shape bonus
        totalPoints += bonus[us]
        if opp == 'A':
            if us == 'X':
                totalPoints += 3
            elif us == 'Y':
                totalPoints += 1
            else:
                totalPoints += 2
        if opp == 'B':
            if us == 'X':
                totalPoints += 1
            elif us == 'Y':
                totalPoints += 2
            else:
                totalPoints += 3
        if opp == 'C':
            if us == 'X':
                totalPoints += 2
            elif us == 'Y':
                totalPoints += 3
            else:
                totalPoints += 1
    print(totalPoints)
