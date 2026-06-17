# STOCK PORTFOLIO TRACKER

# TXT file open and update function
import json
def Saving():
    try:
        with open('C:/Users/Lenovo/Desktop/data.txt','a') as file:
            file.write(json.dumps(Stock)+"\n")
    except FileNotFoundError:
        print("File not Found to save")

# User input stock names and quantity

# defining an empty Dictionary
Stock = {}
num_of = 0


# Requesting input from User for all the Stock data
while True:
    try:
        num_of = int(input("Enter the number of stock you hold : "))
        break
    except ValueError:
        print("\nPlease enter a Number only \n")

# Asking the user for stock information using For loop
if num_of > 0:
    for i in range(num_of):
         name=(input("Enter the name of the Stock : ")).upper()
         while True:
                 try:
                    quantity=(int(input("Enter the Quantity of the Stock : ")))
                    break
                 except ValueError:
                    print("\nPlease enter appropriate characters only \n")
          Stock[name] = quantity
                
else:
    print("You have no Stocks to show ")

if not Stock == {}:
    print("--------------------------------\n")
    print("--------Your Portfolio---------- \n")
    print(f"\t\b{Stock}\t")
    print("--------------------------------\n")
if not Stock == {}:
    save_quit= input("Would you like to Save the DATA (Y/N) : ").upper()[:1]
    Saving()
    print("Your data has been Saved!! ")
        
