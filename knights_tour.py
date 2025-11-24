N=5
moves=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
board=[[0]*N for _ in range(N)]

def valid(x,y): return 0<=x<N and 0<=y<N and board[x][y]==0

def knight(x,y,step):
    board[x][y]=step
    if step==N*N: return True
    for dx,dy in moves:
        if valid(x+dx,y+dy) and knight(x+dx,y+dy,step+1): return True
    board[x][y]=0
    return False

if knight(0,0,1):
    for row in board: print(row)
else: print("No solution")
