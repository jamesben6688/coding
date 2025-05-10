def round_to_significant(x_str, sig_digits):
    x = float(x_str)
    if x == 0:
        return "0"

    from math import log10, floor

    # 计算要保留到小数点后多少位
    digits = sig_digits - int(floor(log10(abs(x)))) - 1
    rounded = round(x, digits)

    # 转为字符串（自动去掉科学计数法）
    result = f"{rounded:.{sig_digits}g}"
    return result
