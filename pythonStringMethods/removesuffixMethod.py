text = "Hello World.jpg"
result = text.removesuffix(".jpg")
print(result)  


#This example shows that if the given suffix does not exist in the specified string, the original string is returned without any modifications −
text = "Hello World"
result = text.removesuffix(".jpg")
print(result) 


#The removesuffix() method, by default, performs a case-sensitive removal. In this instance, the method does not remove the suffix ".jpg" from the string "text" and returns the original string instead −
text = "Hello World.JPG"
result = text.removesuffix(".jpg")
print(result)


text = "Hello World12345"
result = text.removesuffix("12345")
print(result)