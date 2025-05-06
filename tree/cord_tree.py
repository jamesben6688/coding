# class TreeNode:
#     def __init__(self, val, index, left=None, right=None):
#         self.val = val
#         self.index = index
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def get_val(self, root, index):
#         ans = ""
#         def dfs(node):
#             nonlocal ans
#             if node is None:
#                 return ""
#
#             left_str = dfs(node.left)
#             right_str = dfs(node.right)
#
#             if node.index == index:
#                 ans = left_str + right_str
#             return left_str + node.val + right_str
#         dfs(root)
#         return ans
#
# """
# #      InternalNode, 26
# #      /              \
# #     /                \
# #    /                  \
# # Leaf(5, ABCDE)      InternalNode, 21
# #                       /           \
# #                      /             \
# #                     /               \
# #                    /                 \
# #         Leaf(10, FGHIJKLMNO)     Leaf(11, PQRSTUVWXYZ)
#
#
# """
#
# root = TreeNode(
#     "", 1,
#     TreeNode("ABCDE", 2),
#     TreeNode("", 3,
#              TreeNode("FGHIJKLMNO", 4),
#              TreeNode("PQRSTUVWXYZ", 5))
# )
#
# print(Solution().get_val(root, 1))


"""
    cord tree查找和删除
    http://leetcode.com/discuss/post/413991/google-data-structure-to-manipulate-a-ve-5gge/
    https://leetcode.com/discuss/post/1593355/google-phone-interview-rejected-by-anony-r5tf/
"""
class Node:
    def __init__(self, left=None, right=None, is_leaf_node=False, string=""):
        self.is_leaf_node = is_leaf_node
        self.str = string
        self.left = left
        self.right = right
        if is_leaf_node:
            self.length = len(string)
        else:
            self.length = (left.length if left else 0) + (right.length if right else 0)


class Tree:
    def __init__(self, root):
        self.root = root

    def char_at(self, i):
        if i < 0 or i >= self.root.length:
            raise IndexError("String index out of bounds")

        cur = self.root
        while True:
            if cur.is_leaf_node:
                return cur.str[i]
            if i >= cur.left.length:
                i -= cur.left.length
                cur = cur.right
            else:
                cur = cur.left

    def delete(self, start, end):
        if start < 0 or start > self.root.length or start > end:
            raise IndexError("String index out of bounds")
        self._delete(self.root, start, end)

    def _delete(self, node, start, end):
        if start == end:
            return
        if node.is_leaf_node:
            node.str = node.str[:start] + node.str[end:]
            node.length = len(node.str)
            return

        if start >= node.left.length:
            self._delete(node.right, start - node.left.length, end - node.left.length)
        elif end <= node.left.length:
            self._delete(node.left, start, end)
        else:
            self._delete(node.left, start, node.left.length)
            self._delete(node.right, 0, end - node.left.length)

        node.length = node.left.length + node.right.length

    def substring(self, start, end):
        if start < 0 or start > self.root.length or start > end:
            raise IndexError("String index out of bounds")
        return self._substring(self.root, start, end)

    def _substring(self, node, start, end):
        if start == end:
            return ""
        if node.is_leaf_node:
            return node.str[start:end]

        if start >= node.left.length:
            return self._substring(node.right, start - node.left.length, end - node.left.length)
        elif end <= node.left.length:
            return self._substring(node.left, start, end)
        else:
            left_part = self._substring(node.left, start, node.left.length)
            right_part = self._substring(node.right, 0, end - node.left.length)
            return left_part + right_part


if __name__ == "__main__":

    root = InternalNode(LeafNode(5, "ABCDE"),
                        InternalNode(LeafNode(10, "FGHIJKLMNO"),
                                     LeafNode(11, "PQRSTUVWXYZ"), 21),
                        26)

    print(find_cord_at_index(CordTree(root), 6))