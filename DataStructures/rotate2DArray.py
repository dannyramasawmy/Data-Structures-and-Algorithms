

def rotateInPlace(inp: list) -> list:
    """rotates matrix in place
    O(1) in memory
    O(n**2) in time

    Args:
        inp (list): [2D N x N]

    Returns:
        list: [2D N x N]
    """

    # max idx
    lm1 = len(inp[0]) - 1

    for idx in range(len(inp[0]) // 2): 
        for jdx in range(idx, lm1-idx):
            # get all elements / could use pointers in c
            tl = inp[idx][jdx]
            tr = inp[jdx][lm1-idx]
            br = inp[lm1-idx][lm1-jdx]
            bl = inp[lm1-jdx][idx]
            # swap  tl -> bl -> br -> tr -> tl
            tmp = tl
            inp[idx][jdx] = tr
            inp[jdx][lm1-idx] = br
            inp[lm1-idx][lm1-jdx] = bl
            inp[lm1-jdx][idx] = tmp
            # print(f'{tl}, {tr}, {br}, {bl}')
    return inp


def rotateInPlace1L(inp: list) -> list:
    # rotates matrix in place
    return list(list(row) for row in zip(*[row[::-1] for row in inp]))


def comparison(inp: list, out: list, func: "function") -> int:
    """[testing function]

    Args:
        inp (list): [input array]
        out (list): [output comparison]
        func (function): [rotating function]
    """
    try:
        assert func(inp) == out, f"Error: for {func}, arrays are not equal."
        print(f'Pass.')
        return 1
    except:
        print(f'Fail.')
        return 0


if __name__ == "__main__":
    # input matrix
    inp1 = [['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']]

    inp2 = [['a', 'b', 'c', 'd'],
            ['e', 'f', 'g', 'h'],
            ['i', 'j', 'k', 'l'],
            ['m', 'n', 'o', 'p']]

    inp3 = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o'],
            ['p', 'q', 'r', 's', 't'],
            ['u', 'v', 'w', 'x', 'y']]

    # expected output
    out1 = [['c', 'f', 'i'],
            ['b', 'e', 'h'],
            ['a', 'd', 'g']]

    out2 = [['d', 'h', 'l', 'p'],
            ['c', 'g', 'k', 'o'],
            ['b', 'f', 'j', 'n'],
            ['a', 'e', 'i', 'm']]

    out3 = [['e', 'j', 'o', 't', 'y'],
            ['d', 'i', 'n', 's', 'x'],
            ['c', 'h', 'm', 'r', 'w'],
            ['b', 'g', 'l', 'q', 'v'],
            ['a', 'f', 'k', 'p', 'u']]

    ins = [inp1, inp2, inp3]
    outs = [out1, out2, out3]

    # one liner comparison
    counter = 0
    total = 0
    for i, o in zip(ins, outs):
        counter += comparison(i, o, rotateInPlace1L)
        counter += comparison(i, o, rotateInPlace)
        total += 2
    print(f'{counter}/{total} pass')