#构造m*n的矩阵
[0 for _ in range(n)] for _ in range(m)]




###########bfs

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
    
