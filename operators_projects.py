# MY FIRST PROJECTS 

# 🧮 Simple Calculator using Arithmetic Operators
a=float(input("Enter the first number :"))
b=float(input("Enter the second number :"))
print("Addition:",a+b)
print("Suntraction:", a-b)
print("Multipication:",a*b)
print("Division:", a/b)
print("Power:",a**b)
print("Module:",a%b)
print("Floor division",a//b)
 # MY SECOND PROJECTS
# ⚙️ Age Category Checker
age =int(input("Enter your age  :"))
if age<13:
    print("i am child :")
elif age>13 and age<20:
    print("i am Teenage  :")
elif age>20 and age<60:
    print("i am Adult:")
else:
    print("i am senier citizen:")

 # My third project 
# 💰 Salary Bonus Calculator
salary=float(input("Enter your current  salary :"))
performance=input("Enter you performance (good /average/poor):")
if performance=="good":
    salary+=salary*0.20 # 20%
elif performance == "average ":
    salary +=salary*0.10 # 10%
else:
    salary+=salary*0.5 # 5%
print("Your new salary after bonus:", salary)

# My Four project
# 🎓 Student Grade Calculator
print("=== Student Grade Calculator ===")

Urdu=float(input("Eenter the marks in urdu:"))
English=float(input("Eenter the marks in english:"))
Ethics=float(input("Eenter the marks in ethics:"))
Pakistan_study=float(input("Eenter the marks in Pakistan study :"))
Math=float(input("Eenter the marks in math:"))
Physics=float(input("Eenter the marks in physics:"))
Chemistry=float(input("Eenter the marks in chemistry:"))
Bology=float(input("Eenter the marks in bology:"))
Total=Urdu + English + Ethics + Pakistan_study + Math + Physics + Chemistry + Bology
percentage =(Total/1100)*100
if percentage >=80:
    print('A+')
elif percentage >=70:
    print('A')
elif percentage >=60:
    print('B+')
elif percentage >=50:
    print('B')
elif percentage >=40:
    print("C")
else:
    print("Fail")

# Project 5: ATM Simulation System
# 🏧 ATM Simulation Project

balance = 5000  # Initial balance

print("=== Welcome to Rehan Bank ATM ===")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print("Your current balance is:", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount   # Assignment Operator
        print("Money deposited successfully!")
        print("Updated balance:", balance)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:       # Comparison Operator
            balance -= amount       # Assignment Operator
            print("Withdraw successful!")
        else:
            print("Insufficient Balance!")
        print("Remaining balance:", balance)

    elif choice == 4:
        print("Thank you for using Rehan Bank 🏦")
        break

    else:
        print("Invalid option! Please try again.")
