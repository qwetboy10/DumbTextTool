def solve(text):
    words = text.strip().split('\n')
    return [''.join(map(lambda w: w[0], filter(lambda line: len(line) > 0, words)))]

def solve_verbose(text):
    words = text.strip().split('\n')
    min_len = min(map(lambda w: len(w), filter(lambda line: len(line) > 0, words)))
    ret = []
    for i in range(1,min_len):
        ret.append(''.join(map(lambda w: w[i], words)))
    return ret
