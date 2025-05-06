"""
给一个array a[], 称满足a[i] - a[j] = i - j的（i，j）为一个good pair, 找出一共有多少对good pair：
需要clarify的问题有： 1.(i, j) 和(j, i )是否算两对2. 是否考虑 i =j的情况
这题虽然简单， 我一上来却只想到brute force的方法，在面试官提示可以转化为a[i] - i = a[j] - j后才想到可以转为为求新的array b[],
b[i]= a[i] - i中有多少两两相等的数对，由于a[i] - i可能为负数，所以我用了hashmap来统计，
没有用counting array, 最后复杂度是0(n)。 Follow up问了如果是|a[i] - a[j]| =| i - j|的情况怎么办，分类讨论即可

"""