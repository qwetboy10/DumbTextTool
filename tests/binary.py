import collections

def process(binary_list):
    output = []
    while len(binary_list) >= 8:
        output.append(int(''.join(binary_list[:8]),2))
        binary_list = binary_list[8:]
    return bytes(output)

def solve(text):
    freq = collections.Counter(text)
    common = list(map(lambda pair: pair[0], freq.most_common(2)))
    new_text = list(filter(lambda c: c in common, text))
    binary_1 = map(lambda c: str(common.index(c)), new_text)
    binary_2 = map(lambda c: str((common.index(c) + 1) % 2), new_text)
    bytes_1 = process(list(binary_1))
    bytes_2 = process(list(binary_2))
    ret = []
    try:
        ret.append(bytes_1.decode('utf-8'))
    except:
        pass
    try:
        ret.append(bytes_2.decode('utf-8'))
    except:
        pass
    try:
        ret.append(bytes_1.decode('ascii'))
    except:
        pass
    try:
        ret.append(bytes_2.decode('ascii'))
    except:
        pass
    return ret

def solve_verbose(text):
    freq = collections.Counter(text)
    common = list(map(lambda pair: pair[0], freq.most_common(2)))
    new_text = list(filter(lambda c: c in common, text))
    binary_1 = map(lambda c: str(common.index(c)), new_text)
    binary_2 = map(lambda c: str((common.index(c) + 1) % 2), new_text)
    bytes_1 = process(list(binary_1))
    bytes_2 = process(list(binary_2))
    ret = []
    ret.append(bytes_1.hex())
    ret.append(bytes_2.hex())
    return ret
