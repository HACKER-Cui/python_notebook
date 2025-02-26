1、翻转函数
s[i:i+k]=reversed(s[i:k+i])
2、join() 列表转字符串函数
s="".join(s)
str1="ab,sca"
list1=list(str1)
print(list1)
b="".join(list1)
c=" ".join(list1)
print(b)
print(c)
结果：
['a', 'b', ',', 's', 'c', 'a']
ab,sca
a b , s c a

3、list1.reverse()是在list1原地修改，没有返回值
4、for i num in enumerate(nums):取出位置与值
5、ord()
字符转asc码 如print(ord("1")-ord("0"))求某字符数字的值
6、split("x")
以某字符作为分隔符把字符串转成list
str1="ab,sca"
print(list(str1))                 ['a', 'b', ',', 's', 'c', 'a']
print(str1.split(","))             ['ab', 'sca']
