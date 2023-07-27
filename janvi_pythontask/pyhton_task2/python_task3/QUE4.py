ini_list = [[10, 28, 53, 109, 72],
			[46, 38, 48, 39, 21],
			[45, 65, 86, 8, 92, 9]]

num_to_find = 0

res1 = any(num_to_find in sublist for sublist in ini_list)


print(str(res1))