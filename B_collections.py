my_list1 = [1,2,'a', "Hello"]
my_list2 = [1,'a',3,6,7]
my_list1[1] = 67
print(my_list1)
my_list2.append(89)

print(my_list2)
#typle
my_t1 = ('Arnold', 1984)
my_t23 = (1991, 2003)
print(my_t1[1])

#dictionary
my_dict = {
    "name" : "sha",
    "List" : my_list1,
    "tup" : (1,2,3)
    }
my_dict['tup'] = "edjrh"
print(my_dict)

set1 = {1,2,'a',"Hello"}
set2 = {2,3,'b',"Hello"}

union_set = set1 | set2
intersec_set = set1 & set2
diff_set = set1 - set2
sym_diff_set = set2^set1

print(f"Union Set : \t{union_set} \nIntersection Set : \t{intersec_set}\nDifference Set : \t{diff_set}\nSymmetrical Set : \t{sym_diff_set} ")


print(2+2)
print(10/4)
print(10%3)
print(10//3)
print(10**3)
print(1+2*3**2**2//2/2-3)


