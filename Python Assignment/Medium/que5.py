temp_list = []
while True:
    val = input("Element:  ")
    if val.lower() in ['q', 'Q']:
        break
    temp_list.append(int(val))

print(f'Average Tempreature: {sum(temp_list)/len(temp_list)}\n Highest Tempreature: {max(temp_list)} \n Lowest Tempreature: {min(temp_list)}')