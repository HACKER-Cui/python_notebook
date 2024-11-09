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
