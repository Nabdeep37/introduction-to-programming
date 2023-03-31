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
      t =input("total bill:")
      #calculatinf tax
      tax_rate=0.15
    tax =total*tax_rate
    total =total+tax
    print("your total taxes are: ",tax)