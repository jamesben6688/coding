from collections import deque, defaultdict
from datetime import datetime, timedelta


def find_top_image(getVotes, now: datetime):
    # 获取过去 24 小时的所有投票
    votes = getVotes(now - timedelta(hours=24), now)

    # 按时间排序
    votes.sort(key=lambda x: x[1])  # (image_id, vote_time, user_id)

    window = deque()  # 保存当前24小时内的 votes
    count = defaultdict(int)  # image_id -> vote count
    top_image = None
    top_time = None
    max_vote = 0

    for image_id, vote_time, user_id in votes:
        window.append((image_id, vote_time, user_id))
        count[image_id] += 1

        # 移除24小时窗口外的旧 votes
        while window and (vote_time - window[0][1]) > timedelta(hours=24):
            old_image, old_time, _ = window.popleft()
            count[old_image] -= 1
            if count[old_image] == 0:
                del count[old_image]

        # 找当前最大票数 image
        curr_top_image = max(count.items(), key=lambda x: (x[1], -hash(x[0])))[0]
        curr_vote = count[curr_top_image]

        # 如果首次成为top 或发生top切换
        if curr_top_image != top_image:
            top_image = curr_top_image
            top_time = vote_time
            max_vote = curr_vote
        elif curr_top_image == top_image and curr_vote > max_vote:
            # 仍是 top，但票数提升了
            max_vote = curr_vote

    return (top_image, top_time)
