def solve(text):
    return []

def solve_verbose(text):
    words = text.strip().split('\n')
    words = list(filter(lambda line: len(line) > 0, words))
    min_len = max(map(lambda w: len(w),words))
    ret = []
    for i in range(1,min_len):
        ret.append(''.join(map(lambda w: w[i % len(w)], words)))
    return ret
