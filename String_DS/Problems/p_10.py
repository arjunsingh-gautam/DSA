# Count Number of white spaces in string
s=input("Enter a string:")  
print(f"Number of white-space in '{s}':{len(s)-len(s.replace(' ',''))}")
# Time Complexity:O(n)
