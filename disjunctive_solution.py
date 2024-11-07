import pandas as pd
print("Today is sunday or monday.")
x= bool(input("Is today sunday?(true/false)  "))

y= bool(input("Is today monday?(true/false)  "))

if x==True and y==True:
    print("Today is SUnday or monday.")

if x==True and y==False:
    print("Today is Sunday.")

if x==False and y==True:
    print("Today is Monday.")

if x==False and y==False:
    print("Today is others day of the week.")


a=True
b=True
if a==True and b==True:
    c=True
    list.append((a,b,c))

a=False
b=True
if a==False and b==True:
    c=True
    list.append((a,b,c))

a=True
b=False
if a==True and b==False:
    c=True
    list.append((a,b,c))

a=False
b=False
if a==False and b==False:
    c=False
    list.append((a,b,c))

df= pd.DataFrame(list, columns=["a", "b", "c"])
print (df)


