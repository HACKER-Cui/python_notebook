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
24、把一个list转为链表
dummy_head = ListNode(0)
current = dummy_head

# 遍历列表，创建链表
for value in lst:
    current.next = ListNode(value)
    current = current.next

return dummy_head.next  
146、OrderedDict会按插入顺序记录的字典
OrderedDict.move_to_end(key, last=True)
功能: 将指定的键移动到字典的末尾（默认）或开头。
OrderedDict.popitem(last=True)
功能: 删除并返回一个键值对。
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # 使用有序字典
        self.capacity = capacity    # 缓存的最大容量

    def get(self, key: int) -> int:
        if key in self.cache:
            # 将键移动到末尾，表示最近使用
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新值并将键标记为最近使用
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # 如果超过容量，删除最久未使用的键（第一个键）
            self.cache.popitem(last=False)
78、
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path=[]
        self.result=[]
        def backtracking(nums,start_index):
            print(path)
            self.result.append(path[:])#####
避免所有子集共享同一个列表对象的问题是指在编程中，如果你直接将同一个列表对象添加到结果列表中，那么所有这些子集实际上都是对同一个列表的引用。这意味着，如果你修改了任何一个子集，其他的子集也会受到影响，因为它们都是指向同一个列表的引用。
在前面提到的代码中，如果不对path进行复制就直接添加到self.result中，那么所有的子集都会是同一个列表。例如，如果你添加了[1]到path并将其添加到self.result，然后再次添加[1, 2]到path并添加到self.result，那么self.result中的两个子集实际上都是指向同一个列表的引用。如果你随后从path中移除了2，那么self.result中的两个子集都会受到影响，因为它们都是同一个列表。
为了避免这个问题，你需要在将path添加到self.result之前创建path的一个副本。在Python中，你可以使用path[:]来创建一个path的浅拷贝，这样每个子集都是独立的列表，互不影响。这就是为什么在修正后的代码中，我使用了self.result.append(path[:])来确保每个子集都是独立的。这样，即使path被修改了，self.result中的子集也不会受到影响
#############################################          
            print("result=",self.result)
            if(len(path)==len(nums)):
                return None
            for i in range(start_index,len(nums)):
                path.append(nums[i])
                backtracking(nums,i+1)
                path.pop()

        backtracking(nums,0)
        return self.result
173、二叉搜索树迭代器<通过迭代将二叉搜索树转为单调栈>
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left
    def next(self) -> int:
        cur=self.stack.pop()
        node=cur.right
        while node:
            self.stack.append(node)
            node=node.left
        return cur.val
    def hasNext(self) -> bool:
        return len(self.stack)>0
