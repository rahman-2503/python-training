x=int(input("enter the distance"))
if(x<=5):
    print("1")
elif(x%5 == 0):
    print(x/5)
else:
    print(x//5+1)
