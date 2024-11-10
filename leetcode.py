对list1进行翻转，如果list2调用的不是list1的副本，则list2也会被翻转
list2=list1[:]
list1.reverse()
print(list1)
print(list2)
return list1==list2
