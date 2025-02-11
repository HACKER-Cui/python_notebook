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
