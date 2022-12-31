with open('../inputs/day4.txt', 'r') as f:
    contained = 0
    for line in f:
        line = line.strip()
        assignments = line.split(',')
        first = assignments[0].split('-')
        second = assignments[1].split('-')

        # Part 1
        # if int(first[0]) < int(second[0]):
        #     if int(first[1]) >= int(second[1]):
        #         contained+=1
        # elif int(first[0]) > int(second[0]):
        #     if int(second[1]) >= int(first[1]):
        #         contained += 1
        # else:
        #     contained += 1

        if int(first[0]) < int(second[0]):
            if int(first[1]) >= int(second[0]):
                contained+=1
        elif int(first[0]) > int(second[0]):
            if int(second[1]) >= int(first[0]):
                contained += 1
        else:
            contained += 1
    print(contained)

