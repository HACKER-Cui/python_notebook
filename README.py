# python_notebook
牛客
1、从后往前找第一个空格，反向遍历
for ch in reversed(str):
    
    if(ch==' '):
        break    
2、哈希表，转小函数转大函数.upper()
map防止取空值用get方法保护，输入默认值，哈希表如果一开始没有值得先有一个值而不能直接自增
str=input().lower()
str2=input().lower()
count=0
hashmap={}
for ch in str:
        if(ch in hashmap):
            hashmap[ch]+=1
        else:
            hashmap[ch]=1
print(hashmap.get(str2,0))
6、输出一个列表的元素并以空格分隔
for a in list2:
    print(a,end=" ")
8、初始化一个dict 行输入并以空格作为分隔
result=defaultdict(int)
for line in sys.stdin:
print(line)
a = line.split()
a[0]=int(a[0])
a[1]=int(a[1])
对字典以键排序，并输出键值对
sortmap = sorted(result.items())
#print(sortmap)
for a in sortmap:
    print(a[0],a[1])
14、
sorted dic，list在sorted之后都会变为list
21、
python中单个字符串的值是无法改变的，先将其转为list，处理完后用join输出
str1=input()
str1=list(str1)
print(''.join(str1))
51、
输入为1 2 3 4 
先用spilt()取除空格再存入List中这样就是连续的，不会中间有空字符
58、序列取n,k
n,k = list(map(int,input().split()))
num = list(map(int,input().split()))
num = sorted(num)
for i in num[:k]:
    print(i,end=' ')
