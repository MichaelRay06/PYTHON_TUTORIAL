string="Welcome to lagos";
str="o"
new_string= string.rfind(str);#This will start searching from the back
print(new_string)


string="Welcome to lagos";
str="o"
new_string2= string.rfind(str, 6,12);#This will start searching from the back, except when index is used, it search within the given index
print(new_string2)