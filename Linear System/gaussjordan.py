import numpy as np
def gauss_jordan(matrix,n):
        for i in range (n):
            pivot=matrix[i][i]
            for j in range(n+1):
                matrix[i][j]=matrix[i][j]/pivot
                for k in range (n):
                       if(i!=k):
                           factor=matrix[k][i]/matrix[i][i]
                           for l in range (n+1):
                               matrix[k][l]=matrix[k][l]-factor*matrix[i][l]        
        for i in range (n):
            print(matrix[i][n])


def input_output():
    n=int(input("Enter the no of unknowns"))
    matrix=np.zeros((n,n+1))#Creates a matrix or array of size n*n+1 n rows and n+1 columns
    for i in range(n):
        for j in range(n+1):
             matrix[i][j]=float(input("Enter all the coeffiecient of the equation\n"))
        
    print (matrix)#prints the augmented matrix)
    gauss_jordan(matrix,n)
    
input_output()

