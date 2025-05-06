"""
是个data structure design的题，比较复杂，给了两个需要自定义的classes,一个是单一的TreeNode，另一个是Tree,让完成一系列functions,
 包括搭建Tree的function(def initializeTree()), 在Tree里面给定parent node让产生一个新
 TreeNode的function( def createNode(parent):), 随机选择一个node（getRandomNode()),
 还有随机选择一个末梢节点（getRandomLeafNode())

"""
import random
from typing import List, Optional, Set, Dict

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.children: List['TreeNode'] = []

class Tree:
    def __init__(self):
        self.root: Optional[TreeNode] = None
        self.nodes: List[TreeNode] = []       # 所有节点
        self.leaves: Set[TreeNode] = set()    # 当前是叶子的节点
        self.value_map: Dict[int, TreeNode] = {}  # 存储值到节点的映射，支持快速查找

    def initializeTree(self, value: int = 0) -> TreeNode:
        """初始化树并创建根节点"""
        root = TreeNode(value)
        self.root = root
        self.nodes.append(root)
        self.leaves.add(root)
        self.value_map[value] = root
        return root

    def createNode(self, parent: TreeNode, value: Optional[int] = None) -> TreeNode:
        """在指定父节点下创建新节点"""
        new_value = value if value is not None else len(self.nodes)
        node = TreeNode(new_value)
        parent.children.append(node)

        # 更新树状态
        self.nodes.append(node)
        self.leaves.add(node)
        if parent in self.leaves:
            self.leaves.remove(parent)

        self.value_map[new_value] = node
        return node

    def getRandomNode(self) -> TreeNode:
        """等概率返回任意节点"""
        return random.choice(self.nodes)

    def getRandomLeafNode(self) -> TreeNode:
        """等概率返回任意叶子节点"""
        return random.choice(list(self.leaves))

    def findNode(self, value: int) -> Optional[TreeNode]:
        """根据值查找节点"""
        return self.value_map.get(value)

    def deleteNode(self, target: TreeNode) -> bool:
        """从树中删除一个节点，并更新状态"""
        if target == self.root:
            print("Cannot delete root node")
            return False

        # 遍历所有节点，寻找谁是它的父节点
        for node in self.nodes:
            if target in node.children:
                node.children.remove(target)
                break
        else:
            print("Parent not found (invalid tree?)")
            return False

        # 删除该节点及其所有子树（递归）
        def dfs_delete(node: TreeNode):
            self.nodes.remove(node)
            self.value_map.pop(node.value, None)
            self.leaves.discard(node)
            for child in node.children:
                dfs_delete(child)

        dfs_delete(target)

        # 如果 parent 现在没有子节点了，可能成为叶子
        if not node.children:
            self.leaves.add(node)

        return True

    def printTree(self, node: Optional[TreeNode] = None, level: int = 0):
        """打印树的结构"""
        if node is None:
            node = self.root
        print("  " * level + f"Node {node.value}")
        for child in node.children:
            self.printTree(child, level + 1)

# 示例用法
tree = Tree()
root = tree.initializeTree(0)

# 创建子节点
a = tree.createNode(root, 1)
b = tree.createNode(root, 2)
c = tree.createNode(a, 3)

# 随机查询节点和叶子
print("Random node:", tree.getRandomNode().value)
print("Random leaf:", tree.getRandomLeafNode().value)

# 查找节点
print("Find node with value 3:", tree.findNode(3).value)

# 删除节点
print("Deleting node 1...")
tree.deleteNode(a)  # 删除节点 1 和其子树

# 打印树的结构
print("Tree structure after deletion:")
tree.printTree()


