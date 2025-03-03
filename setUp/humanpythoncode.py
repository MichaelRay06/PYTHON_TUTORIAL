def stringCaps(myString):

 capital = []

 statement = myString.split()

 for  word in statement:
      capFirstLetter=word.capitalize()
      capital.append(capFirstLetter)   
      string= " ".join(capital)
      
 return string 

print(stringCaps("hello michal and good morning")) 
#-------------------------------------------------------------------------------------
def stringConsonantCount(strConsonant):

 strConsonant= strConsonant.lower()

 strVowel = ["a", "e", "i"," o ",u" "]

 count =0

 for letter in strConsonant:

        if letter not in strVowel:

           count+=1

 return count

print(stringConsonantCount("Hello World"))
#------------------------------------------------------------------------------

def stringCaps(myString):

 capital = []

 statement = myString.split()

 for word in statement:

     capFirstLetter=word. capitalize()

     capital. append(capFirstLetter)

     string= " ". join(capital)

 return string

print(stringCaps("hello michal and good morning"))
#..#........................................................................

def strDiff_index(strValue):
    count = 0
    valueIndex1 = strValue[0]
    valueIndex2 = strValue[1]

    minLength = min(len(valueIndex1), len(valueIndex2))

    for num in range(minLength):
        if valueIndex1[num] != valueIndex2[num]:
            count += 1

    return count

print(strDiff_index(["abcdef", "defabc"]))