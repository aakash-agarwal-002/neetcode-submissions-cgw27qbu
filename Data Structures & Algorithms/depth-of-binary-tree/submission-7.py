# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        depth = 0
        queue.append(root)
        while len(queue) > 0:
            depth+=1
            print([node.val for node in queue])
            n = len(queue)
            for _ in range(n):
                temp = queue.popleft()
                if temp:
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
        return depth

            
