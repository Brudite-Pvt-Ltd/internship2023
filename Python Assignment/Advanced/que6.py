# class on single inheritance A -> B
class parent_class_single:
    def function1(self):
        print("This is Parent class on single inheritance")

class chile_class_single(parent_class_single):
    def function2(self):
        print("This is Child class on single inheritance")

single_class_obj = chile_class_single()
single_class_obj.function1()
single_class_obj.function2()

print("\n")

# class on miltiple inheritance (A, B) -> C
class parent1_class_multiple():
    def function1(self):
        print("This is parent 1 class on multiple inheritance")

class parent2_class_multiple():
    def function2(self):
        print("This is parent 2 class on multiple inheritance")

class child_class_multiple(parent1_class_multiple, parent2_class_multiple):
    def __init__(self):
        print("This is child  class on multiple inheritance")

multiple_class_obj = child_class_multiple()
multiple_class_obj.function1()
multiple_class_obj.function2()

print("\n")

# class on multilevel inheritance A -> B -> C
class main_class():
    def function1(self):
        print("This is the main class")
class sub_class(main_class):
    def function2(self):
        print("This is the sub class")
class sub_sub_class(sub_class):
    def __init__(self):
        print("This is the sub sub class")

multilevel_class_obj = sub_sub_class()
multilevel_class_obj.function1()
multilevel_class_obj.function2()