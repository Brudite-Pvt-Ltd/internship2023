# program 9 :
    

string = input("Enter the string : ")

new_string = "";

i = 0;
n = len(string);

while(i<n):
    curr = string[i];
    i += 1;
    cnt = 1;
    while( i<n and string[i] == curr ):
        cnt += 1;
        i += 1;
    
    new_string += curr + str(cnt);
    

print("New String : ", new_string)
    