import heapq

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def listify(node, l):
            if node:
                listify(node.left, l)
                l.append(node.val)
                listify(node.right, l)
        l1, l2 = [], []
        listify(root1, l1)
        listify(root2, l2)
        return list(heapq.merge(l1, l2))
