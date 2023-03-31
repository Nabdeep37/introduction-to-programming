a ="Melanie Dental Clinic"
print(a)
b =input("Enter patient's name:")
print(b)
y ="yes"
n ="no"
c =input("Was cleaning performed? (y/n):")
if c==y:
  print("Cleaning rate: $60")
  d =input("Was cavity-filling performed? (y/n):")
  if d==y:
    print("Cavity filling rate: $200")
    e =input("Was X-Ray performed? (y/n):")
    if e==y:
      print("X-Ray rate: $100")
      
      #calculate tax
      total =float(input("total bill:"))
      tax_rate=0.15
    tax =total*tax_rate
    bill =total+tax
    print(bill)
    #for discount
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