对list1进行翻转，如果list2调用的不是list1的副本，则list2也会被翻转
list2=list1[:]
list1.reverse()
print(list1)
print(list2)
return list1==list2
2、set()特点，无序 无重复，可以用来去重，list 可以来排序
可以用
hashset=set()
list3=list(hashset)
list3.sort()去重排序
3、通过 defaultdict(list)来表达有向图，其中list表示一个键指向一个为list的值
node=defaultdict(list)
indeg=[0]*numCourses
result=0
for info in prerequisites:
    node[info[1]].append(info[0])
    indeg[info[0]]+=1
4、通过对字符串转为list排序再输入defaultdict(list)进行49. 字母异位词分组
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1=[]
        if(len(strs)==1):
            list1.append(strs)
            return list1
        dict1=defaultdict(list)
        for i in strs:
            dict1[''.join(sorted(list(i)))].append(i)
        for i,j in dict1.items():
            list1.append(j)
        return list1
127、单词接龙BFS 在queue中绑定步数和单词
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])
        while queue:
            currentWord,steps=queue.popleft()
            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord=currentWord[:i]+c+currentWord[i+1:]
                    if nextWord == endWord:
                        return steps + 1
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        queue.append((nextWord, steps + 1))
        return 0                        
739、通过储存下标实现单调栈，栈在python中就是List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        list1=[0 for _ in range(n)]
        st=list()
        for i in range(n):
            while len(st)!=0 and temperatures[i]>temperatures[st[-1]]:
                t=st.pop()
                list1[t]=i-t
            st.append(i)
        return list1
437、前缀和累加，遍历新数累加到前缀和li
def dfs(self, root, targetSum, path_sums):
        if not root:
            return        
        # 更新当前路径的所有累积和
        new_path_sums = [prev_sum + root.val for prev_sum in path_sums]
        new_path_sums.append(root.val)  # 加入从当前节点开始的新路径
        print(new_path_sums)
        # 统计满足 targetSum 的路径
        self.count += new_path_sums.count(targetSum)
        # 递归处理左右子树
        self.dfs(root.left, targetSum, new_path_sums)
        self.dfs(root.right, targetSum, new_path_sums)

