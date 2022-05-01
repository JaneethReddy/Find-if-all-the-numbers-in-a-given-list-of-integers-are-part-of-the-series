def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return  9*f(n-1) - 11*f(n-2)


def seq_of_num(maxi):
    li = []
    for i in range(maxi//2):
        li.append(f(i))
        if li[-1] > maxi:
            break
    return li

def is_part_of_series(lst):
    seq = seq_of_num(max(li))
    in_list = []
    for i in li:
        if i in seq:
            in_list.append(i)
    return in_list

li = [23,1,4,5,245,298,4009,30240,228061,12093829]
print(is_part_of_series(li))

