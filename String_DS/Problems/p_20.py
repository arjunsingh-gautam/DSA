# reverse odd indexed words
sentence=input("Enter a sentence:")
words=sentence.split(' ')
for x in range(len(words)):
    if x%2!=0:
        words[x]=words[x][::-1]

print(f"Modified sentence:{' '.join(words)}")

# Time Complexity:O(n)
# Space Complexity:O(n)