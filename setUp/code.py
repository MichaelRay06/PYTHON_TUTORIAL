def stringCaps(myString):
 capital = []
 statement = myString.split()
 for  word in statement:
      capFirstLetter=word.capitalize()
      capital.append(capFirstLetter)   
      string= " ".join(capital)
      
 return string 
  
print(stringCaps("hello michal and good morning"))




def stringConsonantCount(strConsonant):

 strConsonant= strConsonant.lower()
 strVowel=["a","e","i","o","u", " "]

 count =0
 
 for  letter in  strConsonant:
        if letter not in strVowel:
         count+=1
      
 return count
 
print(stringConsonantCount("Hello World"))




 
def stringCaps(myString):
 capital = []
 
 statement = myString.split()     

 
 for  word in statement:
      word=word[1:]
    
      
      
      capital.append(word)   
      #string= " ".join(capital)
      
 return capital 
  
    
print(stringCaps("hello michal and good morning"))




def stringCapLetter(myString):

 capital = []
 statement = myString.split()
 
 for  letters in statement:
      firstLetter= letters[0]
      firstLetter.upper()
      
      capital.append(firstLetter.upper())   
      #string= " ".join(capital)
      
 return capital 
 
print(stringCapLetter("hello michal and good morning"))
      