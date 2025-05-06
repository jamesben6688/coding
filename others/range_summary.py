arr = [0,1,2,50,52,75] + [100]

ans = []
left = 0
for i in range(1, len(arr)):
    if arr[i] - arr[i-1] == 1:
        pass
    else:
        if left != arr[i]-1:
            ans.append(f"{left}->{arr[i]-1}")
        else:
            ans.append(left)
    left = arr[i]+1
print(ans)
