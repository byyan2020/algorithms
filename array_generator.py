def array_generator(arr, l, r):
    brr = [max(arr[0], l)]
    cur_diff = brr[0] - arr[0]

    for i in range(1, len(arr)):
        cur_diff += 1
        tmp = max(cur_diff + arr[i], brr[i - 1])
        if tmp > r:
            return -1
        brr.append(tmp)
        cur_diff = brr[i] - arr[i]
    print(brr)

arr = [1, 2, 1, 2]
l = 1
r = 10
array_generator(arr, l, r)