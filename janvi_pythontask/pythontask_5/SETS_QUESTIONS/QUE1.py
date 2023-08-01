#1.Createtwosets:{1,2,3,4}and{3,4,5,6}.Findtheelementsthatareuniquetoeachset
set = {1,2,3,4}
set1= {3,4,5,6}
unique_set = set.symmetric_difference(set1)
print(unique_set)