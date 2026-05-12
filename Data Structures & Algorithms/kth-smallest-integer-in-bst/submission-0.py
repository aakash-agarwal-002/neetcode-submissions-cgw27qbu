# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def count(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + self.count(root.left) + self.count(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        while root:
            left_count = self.count(root.left)

            if k == left_count + 1:
                return root.val

            elif k <= left_count:
                root = root.left

            else:
                k -= left_count + 1
                root = root.right