x = [(1,2,3,None),(5,6,7,8),(1,5,6,None)]


for i in range(len(x)):
    if x[i][3] is None :
        y = list(x[i])
        y[3] = "oui"
        x[i]=tuple(y)

print(x)
