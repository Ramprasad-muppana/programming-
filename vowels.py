n=input("enter your word")
l=len(n)
for i in range(l):
    if n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u':
      #  print("the word contain vowels")
        print("vowel is '{}' at index={}".format(n[i],i))
