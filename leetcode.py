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
