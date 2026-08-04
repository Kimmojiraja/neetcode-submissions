class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for strr in strs:
            sortedstrr = "".join(sorted(strr))
            result[sortedstrr].append(strr)
        return list(result.values())
