from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        N = len(inorder)
        val_to_i_idx = {k: v for v, k in enumerate(inorder)}

        def build(p_start, p_end, i_start, i_end):
            if p_start > p_end:
                return None

            root_val = postorder[p_end]
            root = TreeNode(root_val)
            root_idx = val_to_i_idx[root_val]
            left_size = root_idx - i_start

            root.left = build(p_start, p_start + left_size - 1, i_start, root_idx - 1)
            root.right = build(p_start + left_size, p_end - 1, root_idx + 1, i_end)

            return root

        return build(0, N - 1, 0, N - 1)
