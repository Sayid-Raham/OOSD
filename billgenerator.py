total_revenue = 0
 
while True:
    units = int(input("\nEnter units consumed (-1 to stop): "))
 
    if units == -1:
        break
 
    if units < 0:
        print("Invalid units!")
        continue
 
    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = (100 * 10) + ((units - 100) * 15)
    elif units <= 300:
        bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)
    else:
        bill = (100 * 10) + (100 * 15) + (100 * 20) + ((units - 300) * 25)
 
    print("Electricity Bill: Rs.", bill)
    total_revenue += bill
 
print("\nTotal Revenue: Rs.", total_revenue)
