def promotion(board):
    # Setting empty variables
    output = []
    indexP = 0
    rowK = 0
    indexK = 0
    last_row = board[7]
    # Determining if 'P' is on board
    if 'P' not in board[7]:
        return output
    # Determining if 'K' is not on board
    flag = False
    for index in board:
        if 'K' in index:
            flag = True
            break
    if flag == False:
        return output
    # Finding 'P' position in last row
    for index, line in enumerate(last_row):
        if line == 'P':
            indexP = index
    # Finding the row where 'K' is
    for index, row in enumerate(board):
        if 'K' in row:
            rowK = index
    # Finding the position of 'K' in that line
    for index, line in enumerate(board[rowK]):
        if line == 'K':
            indexK = index
    # Setting the possible occasions and the proper output
    if indexP == indexK or rowK == 7:
        output = ['queen', 'rook']
    elif (rowK == 6 and (indexK == indexP + 2 or indexK == indexP - 2)) or (rowK == 5 and (indexK == indexP + 1 or indexK == indexP - 1)):
        output = ['knight']
    elif (rowK == 6 and (indexK == indexP + 1 or indexK == indexP - 1)) or (rowK == 5 and (indexK == indexP + 2 or indexK == indexP - 2)) or (rowK == 4 and (indexK == indexP + 3 or indexK == indexP - 3)) or (rowK == 3 and (indexK == indexP + 4 or indexK == indexP - 4)) or (rowK == 2 and (indexK == indexP + 5 or indexK == indexP - 5)) or (rowK == 1 and (indexK == indexP + 6 or indexK == indexP - 6)) or (rowK == 0 and (indexK == indexP + 7 or indexK == indexP - 7)):
        output = ['queen', 'bishop']
    else:
        return output
    return output