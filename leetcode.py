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
