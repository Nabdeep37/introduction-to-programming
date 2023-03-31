a ="Melanie Dental Clinic"
print(a)
b =input("Enter patient's name:")
print(b)
y ="yes"
n ="no"
c =input("Was cleaning performed? (y/n):")
if (c==y):
  print("Cleaning rate: $60")
  d =input("Was cavity-filling performed? (y/n):")
  if (d==y):
    print("Cavity filling rate: $200")
    e =input("Was X-Ray performed? (y/n):")
    if (e==y):
      print("X-Ray rate: $100")
      
      #calculate tax
      total =float(input("total bill:"))
      tax_rate=0.15
    tax =total*tax_rate
    bill =total+tax
    print(bill)
    
    #discount
    total =float(input("total bill:"))
    disc1 =0.05
    disc2 =0.1
    if(total>300):
      disc = total * disc2
      total_amount2 =total-disc
      print(total_amount2)
    elif(total>200):
      disc = total * disc1
      total_amount1 =total-disc
      print(total_amount1)
    elif (total<200):
      print(total)

      #takeinput()
a =input("Enter any number:")
b =input("Enter any number:")
operation =input("Enter arithmetic operations:")
#operations=(+,-,*,/)
#displayResult()
if("arithmetic operation"=='++'):
 print(a+b)
elif("arithmetic operation"=='--'):
 print(a-b)
elif("arithmetic operation"=='**'):
 print(a*b)
elif("arithmetic operation"=='/'):
 print(a/b)

 #count a dollar game
penny =1
nickel = 5
dime = 10
quarter = 25
pennies = 100
a = float(input("Enter any penny value :"))
total_cent1 =a*penny
print(total_cent1)
b =float(input("Enter any nickel value :"))
total_cent2 =b*nickel
print(total_cent2)
c =float(input("Enter any dime value :"))
total_cent3 =c*dime
print(total_cent3)
d =float(input("Enter any quarter value :"))
total_cent4 =d*quarter
print(total_cent4)
e =float(input("Enter any pennies value :"))
total_cent5 =a*pennies
print(total_cent5)
#totaldollar
c =total_cent1+total_cent2+total_cent3+total_cent4+total_cent5
print(c)
totaldollar =1.0
if(c>totaldollar):
  print("Sorry, the amount you entered was more than one dollar.")
elif(c<totaldollar):
    print("Sorry, the amount you entered was less than one dollar.")
elif(c==totaldollar):
  print("Congratulation!")/n
  print("The amount you entered was exactly one dollar!")/n
  print("You win the game!!")
 
  