print("===== BILL GENERATOR =====")

name = input("Enter customer name: ")

item1 = input("Enter item 1 name: ")
price1 = float(input("Enter item 1 price: "))
qty1 = int(input("Enter item 1 quantity: "))

item2 = input("Enter item 2 name: ")
price2 = float(input("Enter item 2 price: "))
qty2 = int(input("Enter item 2 quantity: "))

total1 = price1 * qty1
total2 = price2 * qty2

subtotal = total1 + total2
gst = subtotal * 0.18
total = subtotal + gst

print("\n===== BILL =====")
print("Customer:", name)
print("----------------------------")
print(item1, "x", qty1, "=", total1)
print(item2, "x", qty2, "=", total2)
print("----------------------------")
print("Subtotal:", subtotal)
print("GST (18%):", gst)
print("Total Amount:", total)
print("============================")
