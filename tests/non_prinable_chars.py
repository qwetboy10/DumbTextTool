def solve(text):
    ret = []
    for i in range(len(text)):
        c = ord(text[i])
        if (c < 0x20 or c > 0x7e) and c != 0xa and c != 0x9:
            ret.append('Found ' + hex(c) +' at index ' + str(i))
    return ret

def solve_verbose(text):
    return []
