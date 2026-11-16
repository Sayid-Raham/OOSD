stock = 100
total_sold = 0
 
while stock > 0:
    print("\nAvailable Stock:", stock)
    quantity = int(input("Enter quantity sold (-1 to stop): "))
 
    if quantity == -1:
        break
 
    if quantity <= 0:
        print("Invalid quantity!")
        continue
 
    if quantity > stock:
        print("Not enough stock!")
        continue
 
    stock -= quantity
    total_sold += quantity
 
    print("Sale Successful!")
    print("Remaining Stock:", stock)
 
print("\n--- Final Inventory Report ---")
print("Total Units Sold:", total_sold)
print("Remaining Stock:", stock)
