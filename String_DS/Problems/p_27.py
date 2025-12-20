# sort the words in sentence
sentence=input("enter a sentence:")
words=sentence.split(' ')
words.sort()
print(f"sorted by words:{' '.join(words)}")