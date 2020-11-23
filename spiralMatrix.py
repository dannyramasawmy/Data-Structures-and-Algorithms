

def spiral(n: int) -> list:
    """creates a spiral matrix
    O(n**2) in time

    Args:
        n (int): [dimensions]

    Returns:
        list: [2D N x N]
    """
    # initialise
    mat = [[0 for _ in range(n)] for _ in range(n)]

    # max
    lm1 = len(mat[0]) - 1
    num = 0

    # which loop
    for ldx in range(n // 2):
        for side in range(4):
            # which elem
            for edx in range(ldx, lm1 - ldx):
                # num to add
                num += 1
                # switch based on side
                if side == 0:
                    mat[ldx][edx] = num
                elif side == 1:
                    mat[edx][lm1 - ldx] = num
                elif side == 2:
                    mat[lm1 - ldx][lm1 - edx] = num
                else:
                    mat[lm1 - edx][0 + ldx] = num

    # center elem
    if n % 2 == 1:
        mat[n//2][n//2] = n**2

    return mat


def printMat(mat):
    for row in mat:
        print(', '.join([str(elem) for elem in row]))
    return None


def comparison(dimension: int, compare: list, func: "function") -> int:
    """[testing function]

    Args:
        inp (int): [input dimension]
        out (list): [output comparison]
        func (function): [rotating function]
    """
    try:
        assert func(
            dimension) == compare, f"Error: for {func}, arrays are not equal."
        print(f'Pass.')
        return 1
    except:
        print(f'Fail.')
        return 0


if __name__ == "__main__":
    # input matrix
    out0 = [[1, 2],
            [4, 3]]

    out1 = [[1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]]

    out2 = [[1,  2,  3,  4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9,  8,  7]]

    out3 = [[1,  2,  3,  4,  5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]]

    # comparison
    counter = 0
    total = 0

    for n, out in zip([1, 2, 3, 4, 5], [[[1]], out0, out1, out2, out3]):
        counter += comparison(n, out, spiral)
        total += 1

    print(f'{counter}/{total} pass')
