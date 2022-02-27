import numpy as np
import time
import matplotlib as pyplot

l=[0,1,2,3]
n=15
m=15
##########################################################################
#path of output file and opening it
path = '/home/banele/Desktop/HPC/assigment22/myoutfile.txt'
output = open(path,'w')
###########################################################################
A=np.random.randint(0,2,size=(n,m))
np.savetxt('myinfile.txt',A,fmt='%d')
start=time.time()
print(" Reading input file:myinfile.txt")
print("Number of processes: 1")
print("Starting timer...")

for Gen in l:
  sum1=0
  count1=0
###########################################################################
# a loop for outer values
  for i in range(0,n):
   for j in range(0,m):
##############################################################################
# the corners of the gride
    if i==0 and j==0 and A[i,j]>0:
     A[i,j]=A[i,j]-1
    if i==n-1 and j==m-1 and A[i,j]>0:
     A[i,j]=A[i,j]-1
    if i==0 and j==m-1 and A[i,j]>0:
     A[i,j]=A[i,j]-1
    if i==n-1 and j==0 and A[i,j]>0:
     A[i,j]=A[i,j]-1
#############################################################################
# The rest of the boundary
    if i==0 and j>0 and j<m-1:
     count1 = 3+ A[i,j-1]+A[i+1,j-1]+A[i+1,j]+A[i+1,j+1]+A[i,j+1]
    if i==n-1 and j>0 and j<m-1 :
     count1 = 3+ A[i,j-1]+A[i-1,j-1]+A[i-1,j]+A[i-1,j+1]+A[i,j+1]
    if j==0 and i>0 and i<n-1 :
     count1 = 3+ A[i-1,j]+A[i-1,j+1]+A[i,j+1]+A[i+1,j+1]+A[i+1,j]
    if j==m-1 and i>0 and i<n-1 : 
     count1 = 3+ A[i-1,j]+A[i-1,j-1]+A[i,j-1]+A[i+1,j-1]+A[i+1,j]
    if A[i,j] > 0 and count1 == 2 or count1 == 3 :
        A[i,j]=A[i,j]
    if A[i,j]>0 and count1 < 2:
        A[i,j]=A[i,j]-1
    if A[i,j]>0 and count1>3:
        A[i,j]=A[i,j]-1
    if A[i,j]==0 and count1==3:
        A[i,j]=A[i,j]+1  
    sum1=sum1+A[i,j]
#############################################################################
# a loop for the inner values and changing values based on the Game of life rules
  for i in range(0,n-1):
   for j in range(0,m-1):
    
    count2=A[i-1,j+1]+A[i,j+1]+A[i+1,j+1]+A[i+1,j]+A[i-1,j]+A[i+1,j-1]+A[i,j-1]+A[i-1,j-1]
    if A[i,j]>0 and count2<2:
        A[i,j]=A[i,j]-1
    if A[i,j]>0 and count2==2 or count2==3:
        A[i,j]=A[i,j]
    if A[i,j]>0 and count2>3:
        A[i,j]=A[i,j]-1
    if A[i,j]==0 and count2==3:
        A[i,j]=A[i,j]+1  
    sum1=sum1+A[i,j] # calculating count
#############################################################################
# results
  print("Generation",Gen,"number of live cells:", sum1 )
  np.savetxt('output1.txt',A,fmt='%d')
  output.write(" ")
end = time.time()
duration= end - start
print("Total wallclock time:",duration)
print("Writing output file: myoutfile")
output.close()
