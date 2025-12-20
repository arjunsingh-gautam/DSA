# Count Digits:
def count_digits(num):
    count=0
    while num!=0:
        count+=1
        num=num//10
    print(f"no. of digits:{count}")

count_digits(929)