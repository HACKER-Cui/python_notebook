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

0 1 2 3 4 5
2取0 和2 str[]
3取1 和2 
4递归思考架构
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(s, left, right, depth=0):
            # Python 2 compatible string formatting
            print("|  " * depth + "'{}' L:{} R:{}".format(s, left, right),"deep=",depth)          
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right, depth + 1)
            if left > right:
                backtrack(s + ')', left, right + 1, depth + 1)               
        backtrack("", 0, 0)
        return result
("'' L:0 R:0", 'deep=', 0)
("|  '(' L:1 R:0", 'deep=', 1)
("|  |  '((' L:2 R:0", 'deep=', 2)
("|  |  |  '(((' L:3 R:0", 'deep=', 3)
("|  |  |  |  '((()' L:3 R:1", 'deep=', 4)
("|  |  |  |  |  '((())' L:3 R:2", 'deep=', 5)
("|  |  |  |  |  |  '((()))' L:3 R:3", 'deep=', 6)
("|  |  |  '(()' L:2 R:1", 'deep=', 3)
("|  |  |  |  '(()(' L:3 R:1", 'deep=', 4)
("|  |  |  |  |  '(()()' L:3 R:2", 'deep=', 5)
("|  |  |  |  |  |  '(()())' L:3 R:3", 'deep=', 6)
("|  |  |  |  '(())' L:2 R:2", 'deep=', 4)
("|  |  |  |  |  '(())(' L:3 R:2", 'deep=', 5)
("|  |  |  |  |  |  '(())()' L:3 R:3", 'deep=', 6)
("|  |  '()' L:1 R:1", 'deep=', 2)
("|  |  |  '()(' L:2 R:1", 'deep=', 3)
("|  |  |  |  '()((' L:3 R:1", 'deep=', 4)
("|  |  |  |  |  '()(()' L:3 R:2", 'deep=', 5)
("|  |  |  |  |  |  '()(())' L:3 R:3", 'deep=', 6)
("|  |  |  |  '()()' L:2 R:2", 'deep=', 4)
("|  |  |  |  |  '()()(' L:3 R:2", 'deep=', 5)
("|  |  |  |  |  |  '()()()' L:3 R:3", 'deep=', 6)
