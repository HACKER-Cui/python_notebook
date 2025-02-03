1、####构造m*n的矩阵
[0 for _ in range(n)] for _ in range(m)]




2、###########bfs

visited = [[False] * M for _ in range(N)]
from collection import deque()
que=deque()
due.append((N-1,M-1))
direction=[(-1,0),(1,0),(0,-1),(0,1)]:
while que:
  x,y=que.popleft()
  for dx,dy in direction:
    nx,ny=x+dx,y+dy
    if 0<=nx<N and 0<=ny<M and not visted[nx][ny]:
      if data[nx][ny]==".":
        que.append((nx,ny))
        visted[nx][ny]=True
    
3、取中间操作：
当3为位置序列,直接对2整除
0 1 2 3 4 5
2取1  2//2=1
3取1 (3-1)//2+1   
4取2  4//2
5取2  5//2
