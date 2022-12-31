def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

# with open('../inputs/day3_small.txt', 'r') as f:
#     p = 0
#     for line in f:
#         line = line.strip()
#         n = len(line)//2
#         first = set(line[:n])
#         second = line[n:]
#         for c in second:
#             if c in first:
#                 p += priority(c)
#                 break
#     print(p)

with open('../inputs/day3.txt', 'r') as f:
    p = 0
    lines = f.readlines()
    for i in range(len(lines)//3):
        first = set(lines[i*3].strip())
        second = set(lines[i*3+1].strip())
        third = set(lines[i*3+2].strip())
        fs = first.intersection(second)
        final = fs.intersection(third)
        p += priority(list(final)[0])
    print(p)
