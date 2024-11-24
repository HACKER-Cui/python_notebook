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
先用split()取除空格再存入List中这样就是连续的，不会中间有空字符   【split()的用法：把一个str转为不含空格和/n的list】
58、序列取n,k
n,k = list(map(int,input().split()))
num = list(map(int,input().split()))
num = sorted(num)
for i in num[:k]:
    print(i,end=' ')
61放苹果动态规划（第一次看题解做的）
确定边界条件，单层递归相加符合所有条件
76、使用join合并列表为字符串时，首先看看列表是否为str
    for i in range(num):
        list1.append(str(left+2*i))
    print("+".join(list1))
97、字符序列，转换为无空格的int类型的列表   1 2 3 4 5->[1,2,3,4,5]
input().split()去除空格，转为['1','2','3','4','5']
python中的表没有表而是字典defaultdict，而map()函数接受两个参数，第一个参数是一个函数，第二个参数是一个可迭代对象（比如列表）,map() 函数会对可迭代对象中的每个元素应用第一个参数指定的函数。在这个例子中，int 是一个将字符串转换为整数的函数。所以，map(int, input().split()) 会对 input().split() 返回的字符串列表中的每个元素应用 int() 函数，即将每个字符串转换为整数。
返回的是一个map对象，这个对象是一个迭代器，包含了转换后的整数。这个迭代器可以被转换为列表，或者直接在循环中迭代使用。
num_list=list(map(int,input().split())
