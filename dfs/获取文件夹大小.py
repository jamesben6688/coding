def get_filesize(file, path):
    parts = path.strip("/").split("/")
    cur = file

    for p in parts:
        cur = cur[p]

    ans = 0
    if isinstance(cur, int):
        return cur
    else:
        for k in cur:
            ans += get_filesize(cur, k)
        return ans


def delete_path_recursive(tree: dict, path: str) -> bool:
    parts = path.strip("/").split("/")

    def helper(node, parts):
        cur_part = parts[0]
        if cur_part not in node:
            return False

        if len(parts) == 1:
            # 最后一层：删除文件或递归清空目录
            target = node[cur_part]
            if isinstance(target, dict):
                # 先递归清空目录内容
                for key in list(target.keys()):
                    helper(target, [key])
            del node[cur_part]
        else:
            child = node[cur_part]
            if not isinstance(child, dict):
                return False  # 中间路径必须是目录
            deleted = helper(child, parts[1:])
            if not deleted:
                return False
            if not child:  # 目录变为空
                del node[cur_part]
        return True

    return helper(tree, parts)


root = {
            "root": {
                "a.txt": 100,
                "sub": {
                    "b.txt": 200,
                    "nested": {
                        "c.txt": 300
                    },
                    "c.txt": 400
                }
            }
    }



print(get_filesize(root, '/root/sub/c.txt'))
print(delete_path_recursive(root, "/root/sub/nested"))
# print(delete_path_recursive(root, "/root"))
print(root)



