#2.Write a program to rename a key
dict = {'ankita':40, 'ritika':30, 'navpreet':47, 'lakshita':50}
print(dict)
dict["ank"]= dict.pop("ankita")
dict["nav"] = dict.pop("navpreet")
print("after renaming the keys:",dict)