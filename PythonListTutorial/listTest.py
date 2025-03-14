list_indexing = ["london" , "Lagos", "New York", "Toronto", "Paris"]

print( list_indexing[3].upper())
newList= list_indexing[3].upper()
print(newList.isupper())


if len(list_indexing[0]) > len(list_indexing[2]):
     print("The  first is the longest")
else:
     print (" not the longest")



list_indexing[0], list_indexing[-1] = 'Abuja', 'Notherland'
print(list_indexing )

#pairwise swap
list_indexing[0], list_indexing[-1] = list_indexing[-1], list_indexing[0]
print(list_indexing )


#REVERSE LIST
print(list_indexing[: : -1])


#CONVERST LIST TO TUPLE
print(tuple(list_indexing[2:]))