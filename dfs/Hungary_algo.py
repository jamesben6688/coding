from typing import List

def greedy_match(people, questions):
    """
    :param people: List of (person_id, [tags])
    :param questions: List of (question_id, [tags])
    :return: List of matched (person_id, question_id)
    """
    matched = []
    used_questions = set()
    for person_id, person_tags in people:
        for question_id, question_tags in questions:
            if question_id in used_questions:
                continue
            if set(person_tags) & set(question_tags):
                matched.append((person_id, question_id))
                used_questions.add(question_id)
                break  # move to next person
    return matched


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        """
            每次寻找增广路径用dfs: O(V+E)
            寻找m次增光路径: O(M*(V+E)) ~O(M^3)
        """
        m = len(grid)
        n = len(grid[0])
        match = [-1] * n
        visited = [False] * n

        def dfs(i):
            for j in range(n):
                if grid[i][j] == 1:
                    if not visited[j]:
                        visited[j] = True
                        if match[j] == -1 or dfs(match[j]):
                            match[j] = i
                            return True
            return False

        ans = 0
        for i in range(m):
            visited = [False] * n
            if dfs(i):
                ans += 1
        return ans