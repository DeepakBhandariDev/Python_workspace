x=int(input("Enter weight "))
y=input("L for pounds K for kilograms ")
if y.lower()=='l':
    z=x/1.6
    print(z," Kilograms")
elif y.lower()=='k':
    z=x*1.6
    print(z," Pounds")
else: print("Wrong type")