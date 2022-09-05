#4. Write a python script to print first N odd natural numbers

i=1
n=int(input("enter a number"))
while i<=n:
    print(i*2-1,end=' ')
    i+=1