import heapq


def get_largest_dirs(tree, path=""):
    heap = []

    def dfs(node, current_path):
        if node is None:
            return 1  # single file
        total = 0
        for name, child in node.items():
            sub_path = f"{current_path}/{name}" if current_path else name
            total += dfs(child, sub_path)
        # Maintain min-heap of size 10
        if current_path:
            heapq.heappush(heap, (total, current_path))
            if len(heap) > 10:
                heapq.heappop(heap)
        return total

    dfs(tree, "")
    return sorted(heap, reverse=True)  # Top 10 in descending order


tree = {
    "root": {
        "a": {
            "a1.txt": None,
            "a2.txt": None,
            "sub": {"a3.txt": None}
        },
        "b": {
            "b1.txt": None,
        },
        "c": {}
    }
}


# Example usage
top_dirs = get_largest_dirs(tree["root"])
for size, path in top_dirs:
    print(f"{path}: {size} files")
