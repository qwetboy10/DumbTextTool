def solve(text):
    lens = map(lambda word: len(word), text.split())
    return [''.join(list(map(lambda c: chr(c+65),lens)))]

def solve_verbose(text):
    offsets = [0,48,97]
    ret = []
    for offset in offsets:
        lens = map(lambda word: len(word), text.split())
        ret.append(''.join(list(map(lambda c: chr(c+offset),lens))))
    return ret
