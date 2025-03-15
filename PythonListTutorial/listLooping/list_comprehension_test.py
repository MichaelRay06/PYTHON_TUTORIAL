import char

list1 = ['London', 'Lagos', 'Accra', 'New York', 'Toronto']
list2 = ['Nigeria', 'Ghana', 'USA', 'Canada' ,  'Brixton', 'Thamesmead']
list4 =  ['Croydon', 'Liewsham',  'Brixton', 'Thamesmead', 'New Cross']

list7 = ['Nigeria', 'Ghana', 'USA', 'Canada' ,  'Brixton', 'Thamesmead']
list5 =  [6, 7, 8, 9, 0, 1, 14, 18, 2]
list8a =  [0, 1, 3,]
list8b =  [0, 2, 14, 18,]









for index,item in enumerate(list4):
  print (index,item)





def loop_1compresion() :
    list3= [char.upper() for char in list2  if char.isalpha() ]
    return list3
print(loop_1compresion())


def loop_lambda3() :
 list6 = [(lambda x: x*2) (x) for x in list5 if x%2]
 return list6

print(loop_lambda3())


def loop_lambda4() :
 list6 = [(lambda x: x%2) (x) for x in list5 ]
 return list6

print(loop_lambda4())




def nested_loop():
 list11 = list8b
 list12= list8a
 nested_list= [(x,y) for x in list11 for y in list12]
 return  nested_list
print(nested_loop())
print(tuple(nested_loop()))


