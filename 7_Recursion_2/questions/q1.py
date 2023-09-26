from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(string, nextDigits):
            if not nextDigits:
                res.append(string)
                return

            current_letter = nextDigits[0]

            if current_letter != "1":
                for letter in letters[current_letter]:
                    backtrack(string + letter, nextDigits[1:])
            else:
                backtrack(string, nextDigits[1:])

        backtrack("", digits)
        return res


print(Solution().letterCombinations("23"))

