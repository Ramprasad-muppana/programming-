for i in range(4):
    print("\r")
    for j in range(4):
        if j<=i:
            print("*",end="")
        else:
            print("",end="")
