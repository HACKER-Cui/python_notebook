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
