def setZeros(matrix: List[List[int]]) -> None:
    dic_coloumn = {}
    dic_row = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                dic_row[i] = 1
                dic_coloumn[j] = 1

    for i in range(len(matrix)):
        if i in dic_row:
            for j in range(len(matrix[i])):
                matrix[i][j]=0
            continue
        for j in range(len(matrix[i])):
            if j in dic_coloumn:
                matrix[i][j] = 0

        
