#Calculating Vat
print("Calculating Items with VAT")

#Items / Item Statements
item1 = int(input("Please enter how much of item 1 do you want?"))
item2 = int(input("Please enter how much of item 2 do you want?"))

#Cost/ Cost Statement
cost1 = float(input("Please enter the cost for item 1: "))
cost2 = float(input("Please enter the cost for item 2: "))

#Calculations
number_of_item1 = item1 * cost1
number_of_item2 = item2 * cost2
subtotal = number_of_item1 + number_of_item2
vat = subtotal*12/100

#Print Statement for Vat
print("VAT =", vat)

#Print Statement for Total 
Total = subtotal + vat
print("Total =", Total)