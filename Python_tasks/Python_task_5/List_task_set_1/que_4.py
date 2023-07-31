# question 4 - checking for palindrome list

#creating a palindrome list
l = [1, 2, "123", "123",  2, 1]


def palindrome_checker(l):
    i=0;j=len(l)-1
    
    # using two pointers to check palindrome
    while(i<j):
        # reterning false if i'th and j'th elements are not same
        if(l[i] != l[j]):
            return False

        i += 1 
        j -= 1
    # reterning True if it's palindrome
    return True


# calling the function

res = palindrome_checker(l)

if(res):
    print("Palindrome")
else:
    print("Not Palindrome")
