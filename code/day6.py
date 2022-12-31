with open('../inputs/day6.txt', 'r') as f:
    line = f.readline().strip()
    curr = []
    found = False
    for i in range(len(line)):
        c = line[i]
        if c not in curr:
            #Change this to 3 for part 1
            if len(curr) == 13 and not found:
                print(i+1)
                found = True
            else:
                curr.append(c)
        else:
            while curr[0] != c:
                curr = curr[1:]
            curr = curr[1:]
            curr.append(c)

