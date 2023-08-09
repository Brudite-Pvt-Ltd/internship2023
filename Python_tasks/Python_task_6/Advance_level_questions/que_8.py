# program 8 :
    
string = "Robert000Smith000123"

def parse_string(string):
    n=len(string);
    i=0;
    cnt=0;
    rt_dic = {}
    attributes = ['first_name', 'last_name', 'id']
    while(i<n):
        temp = "";
        while(i<n and string[i] != '0' ):
            temp += string[i];
            i += 1;
        
        while(i<n and string[i] == '0'):
            i += 1;
            
        rt_dic[attributes[cnt]] = temp;
        cnt += 1;

    return rt_dic;


print(parse_string(string))        
        
    