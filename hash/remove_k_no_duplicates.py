def remove_common_elements(listA, listB, k):
    """
    给两个list, listA和listB, 一个整数k,
    删除listB中的元素使得新的listB的前k个数与listA的前k个数没有相同的数
    :param listA:
    :param listB:
    :param k:
    :return:
    """
    set_a = set(listA[:k])
    cnt = 0
    for i in range(len(listB)):
        if listB[i] not in set_a:
            listB[cnt] = listB[i]
            cnt += 1

    return listB[:cnt]


def remove_common_elements_followup(lists, k, d):
    s = set()
    cnts = []
    for i in range(len(lists)):
        if i > d:
            s = s-set(lists[i-d][:cnts[i-d]])

        cur_cnt = 0
        for j in range(len(lists[i])):
            if lists[i][j] not in s:
                s.add(lists[i][j])
                lists[i][cur_cnt] = lists[i][j]
                cur_cnt += 1

            if cur_cnt == k:
                break

        cnts.append(cur_cnt)
    print(cnts)

    return [lists[i][:cnts[i]] for i in range(len(lists))]


# 示例
listA = [1, 2, 3, 4, 5]
listB = [3, 4, 6, 7, 8]
listC = [4, 5, 6, 7, 9]
k = 4

result = remove_common_elements(listA, listB, k)
# print(result)

print(remove_common_elements_followup([listA, listB, listC], 4, 2))