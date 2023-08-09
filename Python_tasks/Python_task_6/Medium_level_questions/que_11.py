# program 11 :

lst = ['Red', 'Blue', 'Black', 'White', 'Pink'];

new_lst = list(map( lambda x : list(map( str , x)) , lst))
print(new_lst)