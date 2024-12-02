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
输入为1 2 3 4 (str)-->['1','2','3','4']
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
round(num,1)保留一位小数
102、输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
sorted()：这是一个内置函数，它接受一个可迭代对象作为输入，并返回一个新的、已排序的列表，<原始的可迭代对象不会被改变。>
list.sort()：这是一个列表对象的方法，它直接在原列表上进行排序，不返回任何值（即返回 None），<它会改变原始列表>。
sorted():
iterable: 必需的参数，需要排序的可迭代对象。
key: 可选参数，一个函数，用于从每个列表元素中提取一个用于比较的值。如果没有提供，那么元素本身将被用于比较，相当于每个元素的的优先级
reverse: 可选参数，布尔值。如果设置为 True，则列表元素将被逆序排列，默认为 False。
# 使用 key 参数，例如根据字符串的长度排序
my_strings = ['apple', 'fig', 'banana', 'cherry']
print(sorted(my_strings, key=len))  # 根据字符串长度排序
# 使用 reverse 参数进行降序排序
print(sorted(my_list, reverse=True))  # 降序排序
lamda表达式: x迭代参数：参数返回值
while True:
    try:
        s = input()
        ss = sorted(list(set(s)), key=lambda x:s.count(x)*1000-ord(x), reverse=True)
        print("".join(ss))
    except:
        break
29、映射 常用于密码类题目
import sys
def check(a, b):
    L1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    L2 = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
    result = ""
    if b==1:
        for i in a:
            result+=L2[L1.index(i)]
    if b==-1:
        for i in a:
            result+=L1[L2.index(i)]
    return result
while True:
    try:
        print(check(input(),1))
        print(check(input(),-1))
    except:
        break
45、字典根据值进行排序
dic2=sorted(dic.items(),key=lambda x:x[1],reverse=True)
77、查找字符串中是否有某个字符
if '7' in str(i)
43、迷宫
dfs不要忘了标记已经走过了的路径
def dfs(list1,x,y,row,col,visited,path):
    if(x==row-1 and y==col-1):
        path.append((row-1,col-1))
        for i in path:
            print(f"({i[0]},{i[1]})")
        return
    if list1[x][y] == "1" or visited[x][y]:
        return 
    visited[x][y]=True  
    path.append((x,y))
    if x > 0: 
        dfs(list1, x-1, y, row, col,visited,path)
    if x < row - 1: 
        dfs(list1, x+1, y, row, col,visited,path)
    if y > 0: 
        dfs(list1, x, y-1, row, col,visited,path)
    if y < col - 1: 
        dfs(list1, x, y+1, row, col,visited,path)
    visited[x][y] = False
    path.pop()
107、二分法算精度
a=float(input())
err=0.001
low=min(-1.0,a)
high=max(1.0,a)
ans=(low+high)/2
while abs(ans**3-a)>=err:
    if ans**3<a:
        low=ans
    else:
        high=ans
    ans = (low + high)/2.0  
print(round(ans,1))

