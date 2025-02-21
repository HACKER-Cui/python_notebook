回溯
1、
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path=[]
        result=[]
        #set1=set()
        def backtrack(start,target):
            if sum(path)==target:
                result.append(path[:])
                return
            for i in range(start,len(candidates)):
                #print(i,target)       
                print(path)
                if sum(path)>target:
                    return 
                path.append(candidates[i])
                backtrack(i,target)
                path.pop()
        backtrack(0,target)
        return result
3二分查找
比如，左闭右闭区间和左闭右开区间的区别。在左闭右闭区间中，初始的right是数组的最后一个元素的索引，因此循环条件应该是left <= right，因为当left等于right时，区间仍然有效。而在左闭右开区间中，right是数组长度，此时循环条件应为left < right，因为当left等于right时，区间已经无效了。 然后，中间值的计算。通常用mid = (left + right) // 2，但在left和right很大的时候可能会溢出，所以更安全的写法是mid = left + (right - left) // 2。
二分查找的边界条件可通过统一区间定义和循环不变量来理清思路：

    区间定义（二选一）：

    左闭右闭 [left, right] → 终止条件 left > right
    左闭右开 [left, right) → 终止条件 left == right

    万能模板（左闭右闭）：
口角：等
left, right = 0, len(nums)-1
while left <= right:
    mid = left + (right-left)//2  # 防溢出 mid=(left+right)//2也可以
    if nums[mid] < target:
        left = mid + 1   # 搜索[mid+1, right]
    else:
        right = mid -1   # 搜索[left, mid-1]#因为最后取得是左，所以如果相等要移动右边界
return left  # 首个>=target的位置
