m1=int(input("enter your mark of subject 1 :"))
m2=int(input("enter your mark of subject 2 :"))
m3=int(input("enter your mark of subject 3 :"))

total=m1+m2+m3
print("total",total)

if total>=90:
    print("grade A+")
elif total>=80:
    print(" grade A")
elif total>=70:
    print(" grade A-")
elif total>=60:
    print(" grade B+")
elif total>=50:
    print(" grade B")
elif total>=40:
    print(" grade C")

else:
    print("fail !")
