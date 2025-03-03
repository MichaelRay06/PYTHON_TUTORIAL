str = "This is my lovely home and you are welcome always";

substring= "always";
print(str.endswith (substring , 43, 50)) # it ended at the index before the index of the spcified substring.


substring2= "welcome";
print(str.endswith (substring2 , 35, 42)) # get the range of subtring by inexing range.


print(str.endswith (substring)) # this indicate the sub string is the end of the string but if substring2 is used insted the result will be False as it is not the ending substring.



