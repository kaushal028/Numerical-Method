"""
This program demonstrates a basic implementation of the power method to find the dominant eigenvalue and its corresponding eigenvector 
of any given square matrix of size n*n.

Starting with an initial guess for the eigenvector (which must have at least one non-zero component),the program iteratively solves the equation 
A*x = λ*x. 

In the first iteration, it estimates the dominant eigenvalue (λ), and in subsequent iterations, it refines the eigenvector estimate until the 
change in eigenvalue between iterations is less than a specified error tolerance (0.001).

The power method converges to the dominant eigenvalue and its corresponding eigenvector regardless of the initial guess, provided it is
not the zero vector.
"""


import numpy as np
eigenvalue=0
error=0.001
n=int((input("Size of matrix? \n")))
matrix=np.zeros((n,n))#defining a n*n size matrix
x=np.zeros((n,1))#defining x of size n*1
print("Enter elements for the matrix:\n") 
#Taking input for matrix
for i in range (n):
    for j in range (n):
        print("Enter coefficient for : ",i ," " ,j)
        matrix[i][j]=float(input())
#Taking initial input for eigen vector 
print("Enter Eigen Vector: \n")
for i in range (n):
    x[i]=float(input("Enter elements: "))  
while(True):
    y=np.zeros((n,1))
    for i in range (n):
        for j in range (n):
            y[i]+=matrix[i][j]*x[j]
    emax=abs(y[0])
    for i in range (n):
        if(emax<abs(y[i])):
            emax=y[i]#taking dominant eigen value i.e. one with largest magnitude
    for i in range (n):
        x[i]=y[i]/emax
    temp=abs(eigenvalue-emax)
    eigenvalue=emax
    if(temp<error):#Until the dominant eigen value stabilizes that is doesnt much and the diff between the eigenvalue and emax is less than our error tolerance
        break
print("Eigen Value \n",eigenvalue)
print("Eigen Vector\n",x)