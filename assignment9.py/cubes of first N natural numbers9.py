#9. Write a python script to print cubes of first N natural numbers

n=int(input("enter a number"))
i=1
while i<=n:
    print(pow(i,3),end=' ')
    i+=1