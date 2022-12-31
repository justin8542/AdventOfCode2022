smallBoard = [['N', 'Z'], ['D', 'C', 'M'], ['P']]
largeBoard = [['T','R','G','W','Q','M','F','P'], 
              ['R','F','H'], 
              ['D','S','H','G','V','R','Z','P'],
              ['G','W','F','B','P','H','Q'],
              ['H','J','M','S','P'],
              ['L','P','R','S','H','T','Z','M'],
              ['L','M','N','H','T','P'],
              ['R','Q','D','F'],
              ['H','P','L','N','C','S','D']]

with open('../inputs/day5.txt', 'r') as f:
    for line in f:
        query = line.strip().split(' ')
        f = int(query[3])-1
        t = int(query[5])-1
        amount = int(query[1])
        move = largeBoard[f][:amount]
        #part2 comments out the reverse
        #move.reverse()
        largeBoard[f] = largeBoard[f][amount:]
        largeBoard[t] = move + largeBoard[t]
    for board in largeBoard:
        print(board[0])

