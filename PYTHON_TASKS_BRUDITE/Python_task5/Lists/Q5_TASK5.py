# Q5. Split a list into evenly sized chunks

def chunks(lst, chunk_size):
  
  return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 4
result = chunks(l1, size)
print(result)  
