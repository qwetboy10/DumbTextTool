def solve(text):
    words = text.split('.')
    return [''.join(map(lambda w: w.strip()[0], words))]

def solve_verbose(text):
    words = text.split('.')
    words = list(filter(lambda line: len(line) > 0, words))
    words = list(map(lambda line: line.strip(), words))
    min_len = min(map(lambda w: len(w),words))
    ret = []
    for i in range(1,min_len):
        ret.append(''.join(map(lambda w: w.strip()[i], words)))
    return ret
