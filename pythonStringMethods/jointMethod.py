s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print (s.join( seq ))


Dictionary = {"Player":"Sachin Tendulkar", "Sports":"Cricket"}
# Providing the separator
sep = "MATCH"
# Joining the items in the dictionary with the given string
res = sep.join(Dictionary)
print(res)



sets = {'9','7', '2','9','3','9'}
character = "#"
# storing in the string 
res = character.join(sets)
print(res)