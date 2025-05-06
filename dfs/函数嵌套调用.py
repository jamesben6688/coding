"""

如果输入如下：<1,f1,enter> <2,f2,enter> <3,f2,out> <4,f2,enter><5,f2,out><6,f1,out>
那么需要输出如下：
f1,5
 - f2,1
 - f3,1
要注意的是
1.需要按函数被call的先后顺序输出
2.需要考虑函数的indent。如果f1 里面 call f2，f2 里面再call f3，那么输出f3时前面要有两个空格，
输出f2时前面有一个空格。输出f1时前面没有空格。
"""

def get_output(arr):
    ans = []
    stack = []

    step = 0
    for i in range(len(arr)):
        if arr[i][2] == 'enter':
            stack.append((arr[i], step))
            step += 1
        else:
            ele, _ = stack.pop()
            ans.append(" " * _ + ele[1] + "," + str(arr[i][0]-ele[0])+"\n")
            step -= 1
    return "".join(ans[::-1])


print(get_output([[1,"f1",'enter'],[2,'f2','enter'],[3,'f3','enter'],[4,'f3','out'],[5,'f2','out'],[6,'f1','out']]))