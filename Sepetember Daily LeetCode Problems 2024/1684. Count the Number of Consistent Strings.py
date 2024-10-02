class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = 0
        for i in words:
            flag = True
            for string in i:

                if string in allowed:
                    continue
                else:
                    flag = False
                    break

            if flag == True:
                count += 1

        return count


