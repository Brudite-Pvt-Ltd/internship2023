d1={"mathura":11,"vanarasi":15,"ayodhya":12,"kailash":20 }
MAX=sorted(d1,key=d1.get,reverse=True)[0]
print("the key with max value is :",MAX,"and value is :",d1[MAX])
Min=sorted(d1,key=d1.get)[0]
print("the key with min value is :",Min,"and value is :",d1[Min])