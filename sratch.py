import numpy as np
f = open("temp.txt", "r")
read = [i.strip() for i in f.readlines()]
coords=[]
instructions=[]
flag=0

for r in read:
    if r=='':
        flag=1
        continue
    if flag==1:
        ins=r.split()[2].split('=')
        instructions.append([ins[0],int(ins[1])])
    else:
        coords.append([int(i) for i in r.split(',')])


width,height=0,0
for x,y in coords:
    if x>width:
        width=x
    if y>height:
        height=y


matrix = np.array([[' ']*(width+1) for i in range(height+1)])

for c,r in coords:
    matrix[r][c]='#'

for i,num in instructions:
    if i=='y':
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r>num and matrix[r][c]=='#':
                    matrix[height-r][c]='#'
        
        height = min(num+1,height-1-num)
        matrix=matrix[:height+1,:]
        
    else:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if c>num and matrix[r][c]=='#':
                    matrix[r][width-c]='#'
        
        width = min(num+1,width-num-1)
        matrix = matrix[:,:width+1]


newMat=[]
for m in matrix:
    t=''
    for u in m:
        t+=u
    newMat.append(t)
for m in newMat:
    print(m)








        


