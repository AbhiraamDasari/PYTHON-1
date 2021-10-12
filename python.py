user = input("Enter the Introduction: ")
print(user)
letterCount = 0
wordCount = 1
for I in user:
    letterCount = letterCount+1
    if(I==" "): 
        wordCount = wordCount+1
print(letterCount)   
print(wordCount)
