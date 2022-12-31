with open('../inputs/day1.txt', 'r') as f:
    currSum = 0
    maxSum = []
    for line in f:
        line = line.strip()
        if len(line) == 0:
            if len(maxSum) < 3:
                maxSum.append(currSum)
                maxSum.sort(reverse=True)
            elif maxSum[2] < currSum:
                maxSum[2] = currSum
                maxSum.sort(reverse=True)
            currSum = 0
        else:
            currSum += int(line)
    if currSum > maxSum[2]:
        maxSum[2] = currSum
    print(sum(maxSum))