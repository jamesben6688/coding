import random
import math

def sample_questions(total, ratios, buckets):
    assert len(ratios) == len(buckets)
    ratio_sum = sum(ratios)
    # Step 1: 根据比例计算每个 bucket 应该抽多少题
    raw_counts = [r / ratio_sum * total for r in ratios]
    int_counts = [int(math.floor(c)) for c in raw_counts]

    # Step 2: 修正由于 round 导致的总数不等于 total 的问题
    remaining = total - sum(int_counts)
    # 分配剩下的题目，按照最接近向上取整的值分配
    diffs = [c - i for c, i in zip(raw_counts, int_counts)]
    for i in sorted(range(len(diffs)), key=lambda i: -diffs[i]):
        if remaining == 0:
            break
        int_counts[i] += 1
        remaining -= 1

    # Step 3: 从每个 bucket 随机不放回抽题
    result = []
    for count, bucket in zip(int_counts, buckets):
        if count > len(bucket):
            raise ValueError("Not enough questions in a bucket to sample without replacement.")
        result.extend(random.sample(bucket, count))

    return result
