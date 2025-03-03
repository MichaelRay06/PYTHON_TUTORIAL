str1 = "this is string example....wow!!!";
str2 = "is";

print (str1.rindex(str2))
print (str1.index(str2))



# inputting a string
string = 'Tutorialspoint is a great place to learn Python. Tutorialspoint is an ian company'
# finding the 'Tutorialspoint' using rindex
print(string.rindex('Tutorialspoint'))
# finding the 'is' using rfind
print(string.rindex('is'))



# inputting a string
string = 'Tutorialspoint is a great place to learn Python. Tutorialspoint is an ian company'
# finding the 'Tutorialspoint' using rindex
print(string.rindex('Tutorialspoint', 0, 45))
# finding the 'is' using rfind
print(string.rindex('is', 0, 45))