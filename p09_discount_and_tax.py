# Practical 9: Final amount after discount and tax

price = float(input("Enter product price: "))
discount_percent = float(input("Enter discount (%): "))
tax_percent = float(input("Enter tax (%): "))

discount_amount = price * discount_percent / 100
discounted_price = price - discount_amount
tax_amount = discounted_price * tax_percent / 100
final_amount = discounted_price + tax_amount

print(f"Discount amount  : {discount_amount:.2f}")
print(f"Price after disc.: {discounted_price:.2f}")
print(f"Tax amount       : {tax_amount:.2f}")
print(f"Final amount     : {final_amount:.2f}")
