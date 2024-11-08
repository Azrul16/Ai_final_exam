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


truth_table = []

combinations = [
    (True, True, True),    # Case 1
    (False, True, True),   
    (True, False, True),   
    (False, False, False)  
]

# Populate the truth table with these values
for a, b, c in combinations:
    truth_table.append((a, b, c))

# Create a DataFrame to display the truth table
df = pd.DataFrame(truth_table, columns=["a", "b", "c"])
print(df)


