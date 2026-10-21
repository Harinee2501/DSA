class Solution(object):
    def groupAnagrams(self, strs):
        count=defaultdict(list)
        for i in strs:
            j=tuple(sorted(i))
            count[j].append(i)
        arr=[]
        for i in count:
            arr.append(count[i])
        return arr