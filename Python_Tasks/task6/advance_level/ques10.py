n=3
s = 'ABCDCEFDEFBA'
nl=[]
c=0
st=""
for i in s:
    if (n!=0):
        if i not in nl:
            nl.append(i)
            n-=1
        else:
            nl.remove(i)
            n+=1
    else:
          if i in nl:
            nl.remove(i)
            n+=1
          else:   
            if i not in st: 
                c+=1
                st+=i
            else: 
                st=st.replace(i, '')
           
print(c)        

