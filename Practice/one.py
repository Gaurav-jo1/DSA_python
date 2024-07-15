from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val},{self.left}, {self.right}"

    def __repr__(self):
        return self.__str__()


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node],
            self.sortedArrayToBST(nums[:mid_node]),
            self.sortedArrayToBST(nums[mid_node + 1 :]),
        )

sortedArray = Solution()
print(sortedArray.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7]))
