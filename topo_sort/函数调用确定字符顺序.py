"""
给你一个function，call这个function会返回两个节点的 排序如 a -> b，b -> c。
但是这个function不保证每次返回都是unique的，就是可能返复call 5次，返回的都是 a -> b。
给你总共character的个数n，要求输出character之间的顺序。
我说了解法是先keep call这个function直到见到n个character，或者直到见过 n *(n-1)/2 个relationship。
他说如果告诉了你 a->b, b->c,你不需要 a->c了，我说我不会。
他说保持拓扑排序的时候，在输出所有character之前，queue里面的size只为1，不为1就一直call function。
"""