def list_max(*lists):
    return max(max(lst) for lst in lists)

def list_min(*lists):
    return min(min(lst) for lst in lists)

def list_avg(*lists):
    total = sum(sum(lst) for lst in lists)
    count = sum(len(lst) for lst in lists)
    return total / count
