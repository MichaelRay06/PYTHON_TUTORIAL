string= "welcome to newzealand and I welcome to my to home to in newzealand";

str = "to";

result1= string.find(str); #this returns the index where the substring was found

result2= string.find(str, 38, 45); #it returns the index of the first found substring even if the range specified has mutiple substring. 

result3= string.find(str, 50, 55); #it returns the index of the first found substring even if the range specified has mutiple substring. 

print ("This is result1 :" , result1 )
print ("This is result2 :" , result2 )#
print ("This is result2 :" , result3 )