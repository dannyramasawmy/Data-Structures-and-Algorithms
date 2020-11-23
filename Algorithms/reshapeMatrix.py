

def reshapeMatrix(inMat : "2DList" , outRow : int, outCol : int) -> "2DList":
    """Reshape matrix by packing a list.
    """
    # rows and cols
    inRow = len(inMat)
    inCol = len(inMat[0])

    # check dim
    if (inRow*inCol) != (outRow*outCol):
        print('Incorrect dimensions')
        return inMat

    # initialise
    outMat = []
    tmp = []
    colCount = 0

    for row in inMat:
        for elem in row:
            # add element to temp list
            tmp.append(elem)
            # increment counter
            colCount += 1
            # if counter hits limit (i.e last column of row)
            if colCount == outCol:
                # add the row to the output
                outMat.append(tmp)
                # reset
                tmp = []
                colCount = 0

    return outMat


def reshapeMatrix2(inMat : "2DList" , outRowLen : int, outColLen : int) -> "2DList":
    """Reshape matrix using different method.
    """
    # rows and cols
    inRowLen, inColLen = len(inMat), len(inMat[0])

    # check dim
    if (inRowLen*inColLen) != (outRowLen*outColLen): return inMat

    # convert output matrix i,j index to input i,j  matrix index
    linIdx = lambda i, j: i*outColLen+j 
    row = lambda i,j :  linIdx(i, j)//inColLen
    col = lambda i,j :  linIdx(i, j)% inColLen

    # map elements
    outMat = [[inMat[row(i, j)][col(i, j)] for j in range(outColLen)] for i in range(outRowLen)]

    return outMat


def printMat(matrix : list):
    print('Matrix:')
    for row in matrix:
        print(' '.join(str(elem) for elem in row))




if __name__ == "__main__":

    inp = [ [0, 1, 2],
            [3, 4, 5]]

    # printMat(reshapeMatrix(inp, 3, 4))
    # longer
    printMat(reshapeMatrix(inp, 1, 6))
    printMat(reshapeMatrix(inp, 3, 2))
    # mapping element method
    printMat(reshapeMatrix2(inp, 1, 6))
    printMat(reshapeMatrix2(inp, 3, 2))