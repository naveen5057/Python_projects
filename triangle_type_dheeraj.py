h=int(input("enter first number"))
b=int(input("enter second number"))
p=int(input("enter third number"))
if (h*h==b*b+p*p)or(b*b==h*h+p*p)or(p*p==h*h+b*b):
    print("this is right angle triangle")
elif h!=b!=p:
    print("this is scalene triangle")
elif h==b==p:
    print("this is equilateral triangle")
elif (h==b and h!=p)or(b==p and b!=h)or(p==h and p!=b):
    print("this is isoscales triangle")
