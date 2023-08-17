class shape():
    def area(self, length):
        print(f'Area by SUPER CLASS is {length*length}')
class square(shape):
    def __init__(self, length):
        print(f'Area by SUBCLASS is {length*length}')
        
my_area = square(20)
my_area.area(20)
