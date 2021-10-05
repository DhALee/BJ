def flatten(board):
    return [item for sublist in board for item in sublist]

def solution_old(board, skill):
    answer = 0
    
    for doing in skill:
        # Offense
        if doing[0] == 1:
            target = doing[1:5]
            scale = doing[5]
            range_x = target[2] - target[0]
            range_y = target[3] - target[1]
            for i in range(range_x + 1):
                for j in range(range_y + 1):
                    board[i + target[0]][j + target[1]] -= scale
        # Defense
        elif doing[0] == 2:
            target = doing[1:5]
            scale = doing[5]
            range_x = target[2] - target[0]
            range_y = target[3] - target[1]
            for i in range(range_x + 1):
                for j in range(range_y + 1):
                    board[i + target[0]][j + target[1]] += scale

    for line in board:
        for num in line:
            if num > 0:
                answer += 1
    return answer

def solution(board, skill):
    answer = 0
    board = flatten(board)
    for doing in skill:
        if doing[0] == 1:
            target = doing[1:5]
            scale = doing[5]
            x = target[2] - target[0] + 1
            y = target[3] - target[1] + 1
            for i in range(x * y):
                board[target[0] + i] -= scale
        # Defense
        elif doing[0] == 2:
            target = doing[1:5]
            scale = doing[5]
            x = target[2] - target[0] + 1
            y = target[3] - target[1] + 1
            for i in range(x * y):
                board[target[0] + i] += scale

    
    for num in board:
        if num > 0:
            answer += 1
    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
# solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])