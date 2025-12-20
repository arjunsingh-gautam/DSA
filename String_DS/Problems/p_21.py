# convert each word first char into upper case
sentence=input("Enter a sentence:")
words=sentence.split(' ')
for x in range(len(words)):
    words[x]=words[x].capitalize()

print(f"Modified sentence:{' '.join(words)}")


# Time Complexity:O(n)
# Space Complexity:O(n)