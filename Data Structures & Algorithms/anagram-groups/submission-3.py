class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultt = defaultdict(list)

        for strr in strs:
            sortingg = "".join(sorted(strr))
            resultt[sortingg].append(strr)
        return list(resultt.values())
            
