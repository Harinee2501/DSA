class Solution(object):
    def combinationSum(self, candidates, target):
        def comb(i,target,n,ans,res,candidates):
            if i==n:
                if target==0:
                    res.append(ans[:])
                return
            if(candidates[i]<=target):
                ans.append(candidates[i])
                comb(i,target-candidates[i],n,ans,res,candidates)
                ans.pop()
            comb(i+1,target,n,ans,res,candidates)
        res=[]
        arr=[]
        comb(0,target,len(candidates),arr,res,candidates)
        return res