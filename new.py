h=int(input("enter first number"))
b=int(input("enter second number"))
p=int(input("enter third number"))
if h*h==b*b +p*p or b*b==h*h+p*p or p*p==b*b+h*h:
    print("this is right triangle")
elif h==b==p:
    print("this is equilateral triangle")
elif (h==b and h!=p) or( h==p and b!=h)or(p==h and b!=p):
    print("this is isosceles triangle")
elif h!=b or h!=p:
    print("this is scalene triangle")
