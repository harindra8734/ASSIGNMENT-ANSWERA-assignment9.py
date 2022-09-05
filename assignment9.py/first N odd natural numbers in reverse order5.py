#5. Write a python script to print first N odd natural numbers in reverse order

N=int(input ("enter a number"))
i=N
while i>=1:
    print(i*2-1,end=' ')
    i-=1