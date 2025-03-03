text = "apple,banana,orange,kiwi,tangerine,pear"
result = text.rsplit(',' , 2) # Splits the string from the end and returns a list of substrings.
#print(result)

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
#print(str.split( ))
#print(str.split('\n', ))

str = "aaa,bbb,ccc,ddd,eee, fff,ggg,hhh,jjj,kkk,lll";
#print(str.split(',', 3))

str1 = "Names:\nAlex\nJohn\nRichard\nNick"
#print("String before splitting: " + str1)
#print("String after splitting:")
#print(str1.splitlines())
str2 = "Names:\rAlex\rJohn\rRichard\rNick"
#print("String before splitting: " + str2)
#print("String after splitting:")
print(str2.splitlines())