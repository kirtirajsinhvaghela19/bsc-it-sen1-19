units =int(input("enter the number of unit used :"))
fixed_charge=200

if 500>units:
    charge = 0
else:
    charge = units*100

net_bill = fixed_charge + charge
print(f"net_bill amount : RS.{net_bill}")
