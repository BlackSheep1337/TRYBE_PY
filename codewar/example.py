def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))


print(merge_arrays([1,2,3,4], [7, 7,10,8,9, 13, 0, 25, 15 -10, -30, -25]))

def digital_root(n):
    str_n = str(n)
    if len(str_n) < 2:
        return n
    total = 0
    while len(str_n) > 1:
        for i in range(len(str_n)):
            total += int(str_n[i])
        str_n = str(total)
    return total

print(digital_root(5))

def root_sum(n):
    x = sum(int(i) for i in str(n))
    if x > 9:
       return root_sum(x)
    return x

print(root_sum(5))