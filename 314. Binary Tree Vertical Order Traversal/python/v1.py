from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_left_and_right_side_shift(
        self, node: Optional[TreeNode]
    ) -> Tuple[int, int]:
        temp_root = node

        left = 0
        while node and node.left:
            node = node.left
            left += 1

        node = temp_root

        right = 0
        while node and node.right:
            node = node.right
            right += 1

        return (left, right)

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        left_side_shift, right_side_shift = 0, 0

        row_to_col_to_nodes = {}

        def inorder_traversal(node: Optional[TreeNode], row: int, col: int):
            if node is None:
                return

            nonlocal left_side_shift, right_side_shift

            if left_side_shift < abs(col) and col < 0:
                left_side_shift = abs(col)
            if right_side_shift < col:
                right_side_shift = col

            if row not in row_to_col_to_nodes:
                row_to_col_to_nodes[row] = {}

            if col not in row_to_col_to_nodes[row]:
                row_to_col_to_nodes[row][col] = []

            row_to_col_to_nodes[row][col].append(node.val)

            inorder_traversal(node.left, row + 1, col - 1)
            inorder_traversal(node.right, row + 1, col + 1)

        inorder_traversal(root, 0, 0)

        arr = [[] for _ in range(left_side_shift + right_side_shift + 1)]

        row = 0
        while row in row_to_col_to_nodes:
            cols = row_to_col_to_nodes[row].keys()
            for col in cols:
                arr[col + left_side_shift].extend(row_to_col_to_nodes[row][col])
            row += 1

        return arr
