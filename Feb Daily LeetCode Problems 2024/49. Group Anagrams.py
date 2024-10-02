class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for i in strs:
            x = ''.join(sorted(i))
            # print(x)
            if x not in h:
                h[x]=[i]
                # print(h)
            else:
                h[x].append(i)
        # print(h)
        return(h.values())