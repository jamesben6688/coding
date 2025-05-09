def round_to_significant_digits(num_str, n):
    num = float(num_str)
    if num == 0:
        return "0"

    # 获取数量级
    from math import log10, floor
    magnitude = floor(log10(abs(num)))
    
    # 计算保留的系数
    factor = 10 ** (magnitude - n + 1)
    rounded = round(num / factor) * factor

    # 使用格式控制输出有效数字
    format_str = f"{{:.{n - 1}e}}"
    result = format_str.format(rounded)

    # 判断是否使用指数表示法
    if "e" in result:
        # 尝试转回小数形式，如果可能
        rounded_str = str(int(rounded)) if rounded == int(rounded) else str(rounded)
    else:
        rounded_str = result

    # 移除不必要的尾随小数点
    if "." in rounded_str and rounded_str.endswith("0"):
        rounded_str = rounded_str.rstrip("0").rstrip(".")

    return rounded_str
