
list1= [ 14, 1, 14, 3, 18, 0, 18, 1, 18, 3]




def list_range_comp_loop():
   new_list=  [x for x in range (len(list1)) if x%2==1]
   return new_list
print(list_range_comp_loop())


#def list_range_comp_loop2():

count2 = 0
for count2 in range(len(list1)):
    count2 = count2 + 1
    print(count2)