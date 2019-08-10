def matrixElementsSum(matrix):
    sum = 0
    
            if i == 0:
                sum += matrix[i][j]
                print(matrix[i][j])
            elif matrix[i][j] != 0:for i in range(len(matrix)) :  
        for j in range(len(matrix[i])) :
                print(matrix[i][j])
                check = 1
                for i in range(len(matrix)):
                    if matrix[i][j] == 0:
                        check = 0
                        break
                if check == 1:
                    print(matrix[i][j])
                    sum += matrix[i][j]
    return sum

matrix = [[0,1,1,2], 
         [0,5,0,0], 
         [2,0,3,3]]
print(matrixElementsSum(matrix))
