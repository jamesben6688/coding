"""
given n tasks. 1-n. there is a pair of tasks that will result in unit test failure.
find the pair in fastest way. (3 methods in total, need to make assumption about how to run test)

平均O(nlg(N)), 最坏 O(N^2)
"""

def find_bad_pair_fast(tasks, test):
    def helper(subtasks):
        if len(subtasks) <= 2:
            return tuple(subtasks)
        mid = len(subtasks) // 2
        left = subtasks[:mid]
        right = subtasks[mid:]
        if not test(left):
            return helper(left)
        elif not test(right):
            return helper(right)
        elif not test(left + right):
            # Must be cross-pair
            bad_1 = None
            for a in left:
                if not test([a] + right):
                    bad_1 = a
                    break

            bad_2 = None
            for b in right:
                if not test([bad_1] + [b]):
                    bad_2 = b
                    break
            return [bad_1, bad_2]
        return None
    return helper(tasks)


def make_test_function(bad_pair):
    def test(subtasks):
        # This function fails only on the bad_pair
        return not (bad_pair[0] in subtasks and bad_pair[1] in subtasks)
    return test

# Example tasks and bad pair
tasks = list(range(1, 101))
bad_pair = (23, 77)  # Example bad pair

test_fn = make_test_function(bad_pair)
result = find_bad_pair_fast(tasks, test_fn)

print("Bad pair found:", result)

