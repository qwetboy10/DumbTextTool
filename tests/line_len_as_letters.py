def solve(text):
    lines = text.split('\n')
    lines = map(lambda line: line.strip, filter(lambda line: len(line) > 0, lines))
    lens = map(lambda word: len(word), lines)
    return [''.join(list(map(lambda c: chr(c+65),lens)))]

def solve_verbose(text):
    offsets = [0,48,97]
    ret = []
    for offset in offsets:
        lines = text.split('\n')
        lines = map(lambda line: line.strip, filter(lambda line: len(line) > 0, lines))
        lens = map(lambda word: len(word), lines)
        ret.append(''.join(list(map(lambda c: chr(c+offset),lens))))
    return ret
