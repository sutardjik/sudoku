board=[[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,7,9]]

def find_zero(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]==0:
                return [row,col]
    else:
        return []

def is_valid(board,row,col,value):
    #validity of user input and row check
    if(row<0 or row>len(board[0]) or col<0 or col>len(board[0]) or (value in board[row]) or value>9 or value<1):
        return False
    #col check
    for row_it in range(len(board[0])):
        if value==board[row_it][col]:
            return False
    #3x3 grid check: ranges of rows and cols include (0,3), (3,6), and (6,9)
    for row_num in range((row-(row%3)),(row-(row%3))+3):
        for col_num in range((col-(col%3)),(col-(col%3))+3):
            if value==board[row_num][col_num]:
                return False
    else:
        return True

def solve(board):
    if find_zero(board)==[]:
        return board
    [row,col]=find_zero(board) #retrieval of other empty cells
    for value in range(1,len(board)+1): #values are 1 to 9 inclusive
        if(is_valid(board,row,col,value)):
            board[row][col]=value
            solution=solve(board)
            if solution is not None:
                return solution
    else:
        board[row][col]=0
        return None

def print_board(board):
    for row in range(len(board)):
        rowprint=""
        if(row%3==0):
            print("-------------------------------")
        for col in range(len(board[0])):
            value=board[row][col]
            if(col%3==0):
                rowprint+="|"
            rowprint+=" "+str(value)+" "
        print(rowprint+"|")
    print("-------------------------------")