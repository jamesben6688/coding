import random


def sample_questions(buckets, total, ratio):
    # Step 1: Normalize the ratio
    ratio_sum = sum(ratio)
    norm_ratio = [r / ratio_sum for r in ratio]

    # Step 2: Initial count from ratio (floor first to ensure we don’t overcount)
    counts = [int(total * r) for r in norm_ratio]

    # Step 3: Adjust to make sum(counts) == total
    diff = total - sum(counts)
    # Assign the remaining questions to buckets with largest remainder
    remainders = [(total * r) - int(total * r) for r in norm_ratio]
    for i in sorted(range(len(remainders)), key=lambda i: -remainders[i]):
        if diff == 0:
            break
        counts[i] += 1
        diff -= 1

    # Step 4: Sample from each bucket
    result = []
    for bucket, count in zip(buckets, counts):
        if count > len(bucket):
            raise ValueError("Not enough questions in bucket.")
        result.extend(random.sample(bucket, count))  # no replacement

    return result


bucket1 = ['q1_1', 'q1_2', 'q1_3', 'q1_4', 'q1_5', 'q1_6']
bucket2 = ['q2_1', 'q2_2', 'q2_3', 'q2_4']
bucket3 = ['q3_1', 'q3_2', 'q3_3']

total = 7
ratio = [2, 1, 1]

print(sample_questions([bucket1, bucket2, bucket3], total, ratio))
