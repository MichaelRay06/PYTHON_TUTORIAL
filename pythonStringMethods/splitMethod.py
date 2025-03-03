str1 = "abcde, 12345, !@#$%, 8888, 9999";
str2 = "14<65<189<235<456"
str3 = "abc!de, 12!345, !@#!$%";



print(str1.split(',' , 2)) # split from front 
print(str1.rsplit(',' , 2)) #split from behind
#print(str3.split('!'))
#print(str2.split('<'))