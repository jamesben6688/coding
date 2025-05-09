"""
given n tasks. 1-n. there is a pair of tasks that will result in unit test failure.
find the pair in fastest way. (3 methods in total, need to make assumption about how to run test)

平均O(nlg(N))
"""
def find_bad_pair_O_lgN(tasks, test):
    """

        O(lgN)
    :param tasks:
    :param test:
    :return:
    """
    left = 0
    l = left + 1
    r = len(tasks) - 1

    while l < r:  # [)
        mid = l + (r-l) // 2

        if not test(tasks[left: mid+1]):
            r = mid
        else:
            l = mid + 1
    bad_2 = l

    l = 0
    r = bad_2

    while l < r:  # (]
        mid = l + (r-l+1) // 2
        if not test(tasks[mid:bad_2+1]):
            l = mid
        else:
            r = mid - 1

    bad_1 = l
    return [bad_1, bad_2]




def find_bad_pair_O_N(tasks, test):
    left = 0
    right = len(tasks)-1

    bad_1 = None
    bad_2 = None

    while left <= right:
        if not test(tasks[left: right+1]):
            left += 1
        else:
            bad_1 = left - 1
            break

    while left <= right:
        if not test(tasks[bad_1: right+1]):
            right -= 1
        else:
            bad_2 =  right+1
            break

    return [bad_1, bad_2]

def find_bad_pair_fast(tasks, test):
    """
        O(Nlg(N))
    :param tasks:
    :param test:
    :return:
    """
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
tasks = list(range(0, 101))  # index 从0开始
bad_pair = (2, 77)  # Example bad pair

test_fn = make_test_function(bad_pair)
result = find_bad_pair_fast(tasks, test_fn)
print(find_bad_pair_O_lgN(tasks, test_fn))
print(find_bad_pair_O_N(tasks, test_fn))

print("Bad pair found:", result)

