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

##n=list(map(int,input().split()))
##print(n)
##a=set(n)
##n=list(a)
##print(n)

##units=["inches","yards","milimeters","centimeters","meters","kilometers"]
##c=[12,0.33333,0.000189393939,304.8,0.0003048]
##f=float(input("enter in feets"))
##for i in range(len(units)):
##    print("enter",i+1,"to convert feets into",units[i])
##a=int(input("enter your choice"))
##a=a-1
##b=f*c[a]
##print(f'lenghth in {units[a+1]}={b}')

##def sum_digits(n):
##    s=0
##    while(n>0):
##        r=n%10
##        s=s+r
##        n=n//10
##    return s
##n=int(input(" "))
##a=sum_digits(n)
##print(a)
##

##def first_diff(a,b):
##    m=max(len(a),len(b))
##    for i in range(m):
##        if i>=len(a) or i>=len(b):
##            return i
##        if a[i]!=b[i]:
##            return i
##    return -1
##a=input("")
##b=input("")
##c=first_diff(a,b)
##print(c)


##def is_sorted(n):
##    if n[0]==max(n):
##        for i in range(len(n)-1):
##            if n[i]<n[i+1]:
##                return False
##            else:
##                return True
##    elif n[0]==min(n):
##        for i in range(len(n)-1):
##            if n[i]>n[i+1]:
##                return False
##            else:
##                return True
##    else:
##        return False
##n=list(map(int,input().split()))
##a=is_sorted(n)
##print(a)


