class Solution(object):
    def compress(self, chars):
        j=0
        i=0
        while j<len(chars):
            start=j
            while j<len(chars) and chars[j]==chars[start]:
                j+=1
            count=j-start
            chars[i]=chars[start]
            i+=1
            if count>1:
                for k in str(count):
                    chars[i]=k
                    i+=1
        return i