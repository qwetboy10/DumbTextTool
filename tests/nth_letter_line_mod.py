def solve(text):
    return []

def solve_verbose(text):
    words = text.strip().split('\n')
    min_len = max(map(lambda w: len(w),words))
    ret = []
    for i in range(1,min_len):
        ret.append(''.join(map(lambda w: w[i % len(w)], words)))
    return ret
