text = "Hello World"
result = text.removeprefix("Hello ")
print(result)



#This example shows that if the given prefix does not exist in the specified string, the original string is returned without any modifications −

text = "World"
result = text.removeprefix("Hello ")
print(result)  



#The removeprefix() method, by default, performs a case-sensitive removal. In this instance, the method does not remove the prefix "hello " from the string "text" and returns the original string instead −

text = "HELLO World"
result = text.removeprefix("hello ")
print(result) 