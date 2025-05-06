def find_x(clients, max_log):
    left = 0
    right = max([c[1] for c in clients])
    print(left, right)
    while left < right:  # (]
        mid = left + (right-left+1) // 2
        s = 0
        for c in clients:
            s += min(mid, c[1])

        if s <= max_log:
            left = mid
        else:
            right = mid-1
    return left

clients = [("A", 50), ("B", 20), ("C", 1000), ("D", 50), ("E", 400)]
print(find_x(clients, 303))  # 50+20+90+50+90=300
# 91 50+20+91+91+50+91=303
