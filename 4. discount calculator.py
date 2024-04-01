purchase_amount = float(input("Enter the purchase amount: $"))

if purchase_amount > 100:
    discount = 0.1
elif purchase_amount > 50:
    discount = 0.05
else:
    discount = 0

total_amount = purchase_amount - (purchase_amount * discount)

print("Purchase amount: ${:.2f}".format(purchase_amount))
print("Total amount after discount: ${:.9f}".format(total_amount))