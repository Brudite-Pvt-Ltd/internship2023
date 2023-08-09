
def xyz(st):
    r=[i for i in st.split('0') if len(i)>0]
    
    
    
    
    d={"first name":r[0],"last name":r[1],"id":r[2]}
    return d




s="Robert000Smith000000123"
print(xyz(s))