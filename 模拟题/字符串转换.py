from collections import defaultdict


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True

        m = defaultdict()
        chs = set()
        for i in range(len(str1)):
            ch1 = str1[i]
            ch2 = str2[i]

            if ch1 in m and m[ch1] != ch2:
                return False
            else:
                m[ch1] = ch2
            chs.add(ch2)

        if len(chs) < 26: return True

        return False


print(Solution().canConvert(
str1 =
"abcdefghijklmnopqrstuvwxyz",
str2 =
"bcadefghijklmnopqrstuvwxzz"
))


# from collections import defaultdict, deque
#
# from collections import defaultdict, deque
#
# class Solution:
#     def canConvertWithSteps(self, str1: str, str2: str) -> bool:
#         if str1 == str2:
#             print("✅ 字符串相同，无需转换")
#             return True
#
#         mapping = {}
#         for c1, c2 in zip(str1, str2):
#             if c1 in mapping and mapping[c1] != c2:
#                 print(f"❌ 映射冲突：{c1} -> {mapping[c1]} 和 {c2}")
#                 return False
#             mapping[c1] = c2
#
#         if all(mapping[c] == c for c in mapping):
#             print("✅ 没有实际转换")
#             return True
#
#         used_chars = set(str1) | set(str2)
#         all_chars = set(chr(ord('a') + i) for i in range(26))
#         available_chars = list(all_chars - used_chars)
#         temp_char = available_chars[0] if available_chars else None
#
#         if not temp_char and len(set(str2)) == 26:
#             print("❌ 所有字符已被 str2 占用，且存在环，不能转换")
#             return False
#
#         # Build graph
#         graph = {}
#         for src, dst in mapping.items():
#             if src != dst:
#                 graph[src] = dst
#
#         # Detect cycles using DFS
#         def find_cycles():
#             visited = {}
#             stack = []
#
#             cycles = []
#
#             def dfs(node):
#                 if node not in graph:
#                     return False
#                 if node in visited:
#                     if visited[node] == 1:
#                         idx = stack.index(node)
#                         cycles.append(stack[idx:])
#                     return False
#                 visited[node] = 1
#                 stack.append(node)
#                 dfs(graph[node])
#                 stack.pop()
#                 visited[node] = 2
#
#             for node in graph:
#                 dfs(node)
#             return cycles
#
#         cycles = find_cycles()
#         if cycles:
#             print(f"♻️ 检测到 {len(cycles)} 个环: {cycles}")
#             if not temp_char:
#                 print("❌ 没有可用的临时字符打破环")
#                 return False
#         else:
#             print("✅ 没有环，按拓扑顺序替换即可")
#
#         # 拓扑排序（排除环）
#         indegree = defaultdict(int)
#         rev_graph = defaultdict(list)
#         nodes = set()
#
#         for u, v in graph.items():
#             indegree[v] += 1
#             rev_graph[u].append(v)
#             nodes.add(u)
#             nodes.add(v)
#
#         queue = deque([c for c in nodes if indegree[c] == 0])
#         topo = []
#
#         while queue:
#             u = queue.popleft()
#             topo.append(u)
#             for v in rev_graph[u]:
#                 indegree[v] -= 1
#                 if indegree[v] == 0:
#                     queue.append(v)
#
#         # Add cycle nodes manually (not in topo sort)
#         used = set(topo)
#         for cycle in cycles:
#             for node in cycle:
#                 if node not in used:
#                     topo.append(node)
#
#         # Begin replacing
#         current = list(str1)
#         step = 1
#
#         # Step 1: break all cycles
#         if cycles:
#             for cycle in cycles:
#                 node = cycle[0]
#                 print(f"Step {step}: 用临时字符 '{temp_char}' 打破环 {cycle}")
#                 current = [temp_char if c == node else c for c in current]
#                 print("        " + ''.join(current))
#                 mapping[temp_char] = mapping[node]  # Save final target
#                 mapping[node] = temp_char  # Break the cycle
#                 step += 1
#
#         # Step 2: follow topological order
#         for ch in reversed(topo):
#             if ch not in mapping or mapping[ch] == ch:
#                 continue
#             target = mapping[ch]
#             print(f"Step {step}: 将所有 '{ch}' 替换为 '{target}'")
#             current = [target if c == ch else c for c in current]
#             print("        " + ''.join(current))
#             step += 1
#
#         print(f"✅ 最终结果: {''.join(current)}")
#         return ''.join(current) == str2
#
#
#
# print(Solution().canConvertWithSteps(
# str1 = "abcdef", str2 = "cabefd"
# ))