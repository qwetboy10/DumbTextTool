def solve(text):
    words = text.split('.')
    return [''.join(map(lambda w: w.strip()[0], words))]

def solve_verbose(text):
    words = text.split('.')
    min_len = min(map(lambda w: len(w),words))
    ret = []
    for i in range(1,min_len):
        ret.append(''.join(map(lambda w: w.strip()[i], words)))
    return ret
