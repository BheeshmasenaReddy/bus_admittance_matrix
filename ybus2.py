#inp=input('Enter line data in format of [[from_bus,to_bus,resistance,reactance]] :')
#s1='[[1,2,0,0.2],[2,3,0,0.25],[1,3,0,0.25]]'
s2='[[1,2,0,0.1],[3,4,0,0.1],[1,4,0,0.2],[1,3,0,0.5],[2,3,0,0.2],[1,0,0,0.2]]' #0 bus is ground
linedata=eval(s2)

#Reading linedata
fb=[]
tb=[]
r=[]
x=[]
for i in linedata:
    fb.append(i[0])
    tb.append(i[1])
    r.append(i[2])
    x.append(i[3])
    
z=[complex(r[k],x[k]) for k in range(len(r))] #Calculating primitive impedence
y=[(1/j) for j in z] #Calculating admittance

nbus=max(max(fb),max(tb))
nbranch=len(fb)

ybus=[]

#creating a ybus as null matrix
for i in range(nbus):
    ybus.append([0]*nbus)

#formation of mutual admittance
for i in range(nbranch):
    if fb[i]!=0 or tb[i]!=0:
        ybus[fb[i]-1][tb[i]-1]-=(y[i])
        ybus[tb[i]-1][fb[i]-1]=ybus[fb[i]-1][tb[i]-1]

#formation of self admittance
for m in range(nbranch):
    for n in range(nbranch):
        if (fb[n]-1)==m or (tb[n]-1)==m :
            ybus[m][m]+=y[n]

#function for printing ybus and linedata
def mat_print(lis):
    x=len(lis)
    y=len(lis[0])
    for i in range(x+1):
        for j in range(y+1):
            if i==0 and j==0:
                print("   ",end=" ")
            elif i==0: 
                print(j,end="   ")
            elif j==0:
                print(i,end='  ')
            else:
                print(lis[i-1][j-1],end='  ')
        print("\n")
        
#making input data
inp_data=[]
data=[fb,tb,z]
for i in range(len(linedata)):
    inp_data.append([0]*len(data))
    
for i in range(len(linedata)):
    for j in range(len(data)):
        inp_data[i][j]=data[j][i]

#printing output
print('Adjacency matrix [A] of the given power systems network:')
mat_print(inp_data)
print('\nNo.of buses:',nbus)
print('\nNo. of transmission lines:',nbranch)
for i in range(len(z)):
    print(f'\nPrimitive impedance of line {i+1}:',z[i],'ohms')
print('\nBus admittance matrix:\nYBUS=')
mat_print(ybus)