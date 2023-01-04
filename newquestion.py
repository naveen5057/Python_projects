import re
#email validation
a=1
while a==1:
    txt = input("enter mail id:")
    pattern = "[A-Z]+[a-z]+\d+[@!#$%^&*_]+[@][a-z]{5,7}[.][a-z]{2,3}"
    x= re.search (pattern,txt)
    if re.search(pattern,txt):
        print("valid email-id")
        print(x.string)
    else:
        print("invalid email-id")
