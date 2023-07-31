# program 7 : set division

# creating two sets A and B

set_A = {10, 20, 30}
set_B = {2, 5, 10}

# if a is divisible by b then adding it to set_divi
set_divi = { (a, b) for a in set_A for b in set_B if (a%b) == 0 }

print(set_divi)
