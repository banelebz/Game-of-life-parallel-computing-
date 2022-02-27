from mpi4py import MPI
import numpy as np
import time
comm = MPI.COMM_WORLD
size1 = comm.Get_size()
rank = comm.Get_rank()

l=[0,1,2,3,]
n=15
m=15
######################################################################################
# At this point I'm making the intial input(the )
A=np.random.randint(0,2,size=(n,m))
B=np.random.randint(0,1,size=(n,m))
np.savetxt('myinfile.txt',A,fmt='%d')
######################################################################################
p=size1
k=p-1
#####################################################################################
# starting time
start=time.time()
#####################################################################################
if rank==0:
 print("Reading input file:myinfile.txt")
 print("Number of processes:",p)
 print("Starting timer...")

for Gen in l:
 for g in range (1,p): # a loop for the processings
  if rank == g:
   B=np.random.randint(0,1,size=(n,m))
   for a in range(0,p-2): # a loop I used to the grid into sub-gribs
     sum1=0
     count1=0 
     for i in range(0,n): # a loop for the matrix i used surrounding
      for j in range(0,m):# a loop for the matrix i used surrounding
##########################################################################
# The corners of the grid        
       if i==0 and j==0 and A[i,j]>0:
        A[i,j]=A[i,j]-1
       if i==n-1 and j==m-1 and A[i,j]>0:
        A[i,j]=A[i,j]-1
       if i==0 and j==m-1 and A[i,j]>0:
        A[i,j]=A[i,j]-1
       if i==n-1 and j==0 and A[i,j]>0:
        A[i,j]=A[i,j]-1
############################################################################
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
###########################################################################################
# We start the inner loop here   
     for i in range(0,n-1):
      for j in range(a*int(m/k),((a+1)*int(m/k))): # I used the "a" to divide the grid and giving the processing a sub-grid    
       count2=A[i-1,j+1]+A[i,j+1]+A[i+1,j+1]+A[i+1,j]+A[i-1,j]+A[i+1,j-1]+A[i,j-1]+A[i-1,j-1] # a count
##############################################################################################
# rules
       if A[i,j]>0 and count2<2:
         A[i,j]=A[i,j]-1
       if A[i,j]>0 and count2==2 or count2==3:
         A[i,j]=A[i,j]
       if A[i,j]>0 and count2>3:
         A[i,j]=A[i,j]-1
       if A[i,j]==0 and count2==3:
         A[i,j]=A[i,j]+1  
       sum1=sum1+A[i,j]
       B[i,j]=A[i,j]
#############################################################################################
#sending the grid to processors 0
 if rank ==p-1:
  comm.Send(B,dest=0, tag=11)
############################################################################################## 
 if rank ==0: 
  B=np.random.randint(0,1,size=(n,m))
  comm.Recv(B, source=p-1, tag=11)
  sum2=0
  for i in range(0,n):
   for j in range(0,m):
    sum2=sum2+B[i,j]
####################################################################################
  print("Generation",Gen,"number of live cells:", sum2 )
  np.savetxt('output11.txt',B,fmt='%d')
end = time.time()
duration= end-start
if rank ==0:
  print("Total wallclock time:",duration)
  print("Writing output file: myoutfile")  
