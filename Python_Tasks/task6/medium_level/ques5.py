t_r = [25, 28, 21, 24, 27]
MAX=-1e8
MIN=1e8
AVG=0
for i in t_r:
    AVG+=i
    if i > MAX:
        MAX=i
    elif i<MIN :
        MIN=i
        
print("average temprature is : ",AVG/len(t_r) )
print("maximum temprature is : ",MAX)
print("minimum temprature is : ", MIN)        