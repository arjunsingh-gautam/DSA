# convert except first and last char into upper case
sentence=input("Enter a sentence:")
words=sentence.split(' ')
result=[]
for x in range(len(words)):    
  result.append((words[x][0]+words[x][1:len(words[x])-1].upper()+words[x][-1]))

print(f"Modified sentence:{' '.join(result)}")