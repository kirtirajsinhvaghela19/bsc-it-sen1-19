grade=input("enter your grade (A,B,C,D,F ):")
grade=grade.upper()
if grade=="A":
    print("excellent")
elif grade=="B":
    print("good")
elif grade =="C":
    print("average")
elif grade=="D":
    print("pass")
elif grade=="F":
    print("fail !")
else:
    print("inverid grade !")