string = "This is my lovely home and you are welcome always";

substring= "welcome always";
print(string.find(substring, 20, 49)) # find from index 35


substring2= "ome";
print(string.count (substring2)) # Number of times the substring found in the wholw string.

substring3= "is";
print(string.count (substring3, 0, 20 )) # number of time the substring find in the specified inex ranges.

substring4= "home";
print(string.count (substring4, 0, 30 )) # number of time the substring find in the specified inex ranges.

substring5= "home";
print(string.count (substring5, 40 )) # if the substring is not  find in the specified index ranges it returns -1.




