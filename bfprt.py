def median_index(sorted_array):
    return (len(sorted_array) - 1) // 2

def median(sorted_array):
    return sorted_array[median_index(sorted_array)]

def bfprt(arr, k, r=5):
    if len(arr) <= r:
        return sorted(arr)[k]

    sublists = [arr[i:i + r] for i in range(0, len(arr), r)]
    medians = [median(sorted(sublist)) for sublist in sublists]

    pivot = bfprt(medians, len(medians) // 2, r)

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(low):
        return bfprt(low, k, r)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return bfprt(high, k - len(low) - len(equal), r)

def select_bfprt(x, y, z, r=5):
    if z < 1 or z > y:
        raise ValueError("z fora dos limites")
    return bfprt(x, y - z, r)