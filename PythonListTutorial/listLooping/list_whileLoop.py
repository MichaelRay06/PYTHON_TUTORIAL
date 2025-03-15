import char

list1 = ['London', 'Lagos', 'Accra', 'New York', 'Toronto']
list2 = ['Nigeria', 'Ghana', 'USA', 'Canada' ,  'Brixton', 'Thamesmead']
list4 =  ['Croydon', 'Liewsham',  'Brixton', 'Thamesmead', 'New Cross']

list5 =  [5, 6, 7, 8, 9, 0]




count2 = 0
for count2 in range(len(list1)):
    count2 = count2 + 1
    print(count2)


count=0
while  count < len(list1):
    count += count
   # print(count)




count1 = 0
while count1 in range (len(list1)):
        count1 += count1
        #print(count1)


list3= [char.upper() for   char in list2  if char.isalnum() ]
#print(list3)

for index,  item in enumerate(list4):
    print(index, item)
