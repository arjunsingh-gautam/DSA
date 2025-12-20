# convert even length words into upper case
sentence=input("Enter a sentence:")
words=sentence.split(' ')
for x in range(len(words)):
    if len(words[x])%2==0:)
        words[x]=words[x].upper()

print(f"Modified Word:{' '.join(words)}")

# Time Complexity=O(n)
# Space Complexity=O(n)
