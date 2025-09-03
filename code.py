a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=a+b+c+d+e
if f>=95:
    print("Grade A")
elif f>=75:
    print("Grade B")
elif f>=50:
    print("Grade C")
if f<50:
    print("Grade D")
print("Total Marks :" , f )
print("Average Marks :" , f/5)