# program 10 :

n = int(input("Enter the Number : "))
string = input("Enter the String : ")

st = []
ans = 0;

count = {}

for x in string:
    count[x] = count.get(x, 0) + 1
    if len(st) > 0 and  x == st[len(st)-1] :
        st.pop()
    elif len(st) < n :
        if count[x]&1 : 
            st.append(x)
    else:
        ans += 1

print(ans)