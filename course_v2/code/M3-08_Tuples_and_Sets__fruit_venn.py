# M3-08_Tuples_and_Sets - fruit_venn.py
class_a = {"apple", "mango", "kiwi", "banana"}
class_b = {"mango", "grape", "banana", "pear"}
print("Both:", sorted(class_a & class_b))
print("Either:", sorted(class_a | class_b))
print("Only A:", sorted(class_a - class_b))
