str=input("Enter a string: ")
a=input("Enter a Character: ")[0]
i=0
for el in str:
    if(el==a):
        i+=1

print("\nNumbers of occurrence of the character in a string: ", i)
