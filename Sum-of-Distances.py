1class Solution(object):
2    def distance(self, nums):
3        n = len(nums)
4        arr = [0] * n
5        count = defaultdict(list)
6        for i in range(n):
7            count[nums[i]].append(i)
8        for val in count:
9            pos = count[val]
10            k = len(pos)
11            prefix = [0] * k
12            prefix[0] = pos[0]
13            for i in range(1, k):
14                prefix[i] = prefix[i-1] + pos[i]
15            for i in range(k):
16                idx = pos[i]
17                if i > 0:
18                    left = pos[i] * i - prefix[i-1]
19                else:
20                    left = 0
21                if i < k - 1:
22                    right = (prefix[k-1] - prefix[i]) - pos[i] * (k - i - 1)
23                else:
24                    right = 0
25
26                arr[idx] = left + right
27        return arr