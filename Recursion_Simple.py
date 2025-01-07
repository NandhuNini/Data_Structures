# Factorial 

a=5
def fact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1)
print(fact(a))

# Sum of n natural numbers

n=10
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(n))
    
#Print numbers to 1 to n

def number(n,current=1):
    if current>n:
        return
    print(current)
    number(n,current+1)
n=int(input("Enter the number"))
number(n)

#print numbers n to 1

def reverse(n):
    if n==0:
        return
    print(n)
    reverse(n-1)
n=int(input("Enter the number:"))
reverse(n)

