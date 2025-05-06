from collections import defaultdict

def compute_visible_area_by_pixel(screen_size, windows):
    W, H = screen_size
    screen = [[None for _ in range(W)] for _ in range(H)]

    # 按 z-order 升序处理（低的先画，越高的越后盖住）
    sorted_windows = sorted(windows.items(), key=lambda x: x[1][2])

    for name, ((x1, y1), (x2, y2), z) in sorted_windows:
        # 限制在屏幕内（防止越界）
        x1 = max(0, min(x1, W))
        x2 = max(0, min(x2, W))
        y1 = max(0, min(y1, H))
        y2 = max(0, min(y2, H))

        for y in range(y1, y2):
            for x in range(x1, x2):
                screen[y][x] = name  # 后面的窗口会覆盖前面

    # 统计归属
    area_count = defaultdict(int)
    for row in screen:
        for cell in row:
            if cell:
                area_count[cell] += 1

    return dict(area_count)
