print("Welcome To Password Strength Checker 💗")
pas = input("Enter a password here: ")
satisfied = 0
if (len(pas) >= 8):
    con1="✅ The length of the password is Acceptable"
    satisfied+=1
else:
    con1="❌ The password is short, it must be 8 characters..."

print(con1)

cap = 0
low = 0
for i in range(len(pas)):
    a = pas[i].isupper()
    if a==True:
        cap += 1
    else:
        low += 1

if low==len(pas):
    con2 ="❌ There must be one uppercase character in the password"
else:
    con2="✅ The uppercase condition is satisfied"
    satisfied+=1
print(con2)

if cap==len(pas):
    con3 ="❌ There must be one lowercase character in the password"
else:
    con3="✅ The lowercase condition is satisfied"
    satisfied+=1
print(con3)

# alnum = pas.isalnum()
# if alnum ==True:
#     con4="✅ The password is Alphanumeric"
# else:
#     con4="❌ The password must contain atleast one degit and avoud spaces"
# print(con4)

alnum = 0
for j in range(len(pas)):
    num=pas[j].isnumeric()
    if num==True:
        alnum+=1
    
if 0<alnum<len(pas):
   con4="✅ The password is Alphanumeric"
   satisfied+=1
elif alnum ==len(pas):
    con4="❌ The password must contain elements otherthan digits too, only numbers are not allowed"
else:
    con4="❌ The password must contain atleast one degit"
print(con4)

sc=0
for k in range(len(pas)):
    if pas[k]=="!":
        sc+=1
    elif pas[k]=="@":
        sc+=1
    elif pas[k]=="#":
        sc+=1
    elif pas[k]=="$":
        sc+=1
    elif pas[k]=="%":
        sc+=1
    elif pas[k]=="^":
        sc+=1
    elif pas[k]=="&":
        sc+=1
    elif pas[k]=="*":
        sc+=1

if sc == 0:
    con5 = "❌ There must be an Special Character such as: !, @, #, $, %, ^, &, *"
elif sc ==len(pas):
    con5 = "❌ The password can not contain only special characters"
else:
    con5="✅ The password contains Special characters"
    satisfied+=1
print(con5, "\n")

if satisfied==1:
    print("⭐")
    print("⚠ Password Strength: Weak")
elif satisfied==2:
    print("⭐⭐")
    print("⚠ Password Strength: Weak - Medium")
elif satisfied==3:
    print("⭐⭐⭐")
    print("⚠ Password Strength: Medium")
elif satisfied==4:
    print("⭐⭐⭐⭐")
    print("⚠ Password Strength: Medium - Strong")
elif satisfied==5:
    print("⭐⭐⭐⭐⭐")
    print("⚠ Password Strength: Strong")