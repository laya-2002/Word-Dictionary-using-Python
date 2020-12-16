  # Word Dictionary in Python 

word=input() 

  # Writing URL's in double quotes

mean1=("\"https://en.m.wikipedia.org/wiki/")+(word)+("\"")
mean2=("\"https://dictionary.cambridge.org/dictionary/english/")+(word)+("\"")
  
  # Creating dictionary to represent word and meanings. 

URL1={word:mean1} 
URL2={word:mean2} 

  # Displaying the URL's. 

print("$ ",meaning1[word],"\n")
print("$ ",meaning2[word],"\n") 
print("\nClick on the above URL's to know the meaning.") 
