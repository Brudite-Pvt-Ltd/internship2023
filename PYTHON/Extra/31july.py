# def func1(i):
#     def inner(i):
#         return i**3
#     return inner

# @func1
# def func2(i):
#     return i

# print(func2(2))

# f = open('/media/asifreak/TOOLS/github/brudite/internship2023/PYTHON/Extra/sample.txt', 'r')
# list = []
# for i in f:
#     list.append(i)
# print(list[4])
# f.close()

with open('/media/asifreak/TOOLS/github/brudite/internship2023/PYTHON/Extra/sample.txt', 'r') as fe:
    for i in fe:
        print(i)