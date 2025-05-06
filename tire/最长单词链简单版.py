"""
给你一个string set，比如：（den，dent，dents，dew，det，bet，bent），找到最长的递增string list，递增的规则是前一个string尾部
增加一个字母变成后一个string。
例子的output是：den-》dent-》dents


这题用tire建立字典树。然后找最长的路径即可
"""
