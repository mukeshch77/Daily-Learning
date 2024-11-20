list=[34,56,78,98,67,45,23]

L_no=list[0]
for el in list:
    if(el>=L_no):
        L_no=el

print("List: ", list)
print("\nLargest number in a list: ",L_no)