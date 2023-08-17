user_list = []
while True:
    val = input("Element:  ")
    if val.lower() in ['q', 'Q']:
        break
    user_list.append(int(val))

k = int(input("Enter vlaue for K:  "))

pair_list = []

for i in range(len(user_list)):
    a = user_list[i]
    for j in range(len(user_list)):
        b = user_list[j]
        if (a + b == k) & (user_list.index(a)!=user_list.index(b)):
            pair_list.append([a,b])

print(pair_list)
print(f'Pair count: {len(pair_list)/2}')
