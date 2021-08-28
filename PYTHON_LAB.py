##a=float(input(" enter "))
##b=float(input(" enter "))
##if a>b:
##    c=a-b
##else:
##    c=b-a
##if c<=0.001:
##    print("close")
##else:
##    print("not close")
##

##a=input(" ")
##for i in a:
##    if i in "AEIOUaeiou":
##        print(i)

##a=input("ente r")
##b=input("enter")
##if len(a)==len(b):
##    for i in range(len(a)):
##        print(a[i],end=" ")
##        print(b[i],end=" ")
##else:
##    print("differ")

##n=int(input(""))
##print("{:,}".format(n))

##a=input("enter ")
##for i in range(len(a)-1):
##    if a[i].isdigit():
##        if a[i+1]!=")":
##            print(a[i],end=" ")
##            print("*",end=" ")
##        else:
##            print(a[i],end=" ")
##    else:
##        print(a[i],end=" ")
##if i==len(a)-2:
##    print(a[i+1],end=" ")

##import random
##b=[]
##e=0
##for i in range(20):
##    a=random.randint(1,100)
##    b.append(a)
##    if a%2==0:
##        e+=1
##        
##print(b)
##avg=sum(b)/20
##print(avg)
##c=max(b)
##d=min(b)
##print("max:",c,"min",d)
##b.remove(c)
##b.remove(d)
##b=set(b)
##b=list(b)
##c=max(b)
##d=min(b)
##print("max",c,"min:",d)
##print(e)

##a=[]
##n=int(input("enter the number"))
##for i in range(1,n+1):
##    if n%i==0:
##        a.append(i)
##print(a)        

##import random
##a=[]
##l=[]
##c=1
##n=int(input(" enter "))
##for i in range(n):
##    a.append(random.randint(0,1))
##print(a)
##for i in range(len(a)-1):
##    if a[i]==a[i+1] and a[i]==0:
##        c+=1
##
##    else:
##        l.append(c)
##        c=1
##else:
##    l.append(c)    
##print(max(l))

n=list(map(int,input().split()))
print(n)
a=set(n)
n=list(a)
print(n)
