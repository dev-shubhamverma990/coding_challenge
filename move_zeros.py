"""Move all 0s to the end while maintaining order"""


def move_zeros(lst):
    non_zero = [x for x in lst if x != 0]
    zero_count = lst.count(0)
    return non_zero + [0] * zero_count

def _move_zeros(lst):
    non_zero = []
    zero_count = 0
    for x in lst:
        if x != 0:
            non_zero.append(x)
        else:
            zero_count += 1
    return non_zero + [0] * zero_count

if __name__ == "__main__":
    lst = [0, 1, 0, 3, 12]
    print(move_zeros(lst))
    print(_move_zeros(lst))