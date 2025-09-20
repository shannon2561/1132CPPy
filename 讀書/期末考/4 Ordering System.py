# 24 mins

for _ in range(int(input())):
    Name = input()
    print("Customer:",Name)
    n = int(input())
    print("Number of Items:", n)
    print("Order Details:")

    total = 0
    for i in range(n):
        data = input().split(";")
        food = data[0]
        quantity = int(data[1])
        price = float(data[2])
        discount = data[3]
        if discount == "DISC10":
            subtotal = quantity * price * 0.9
        elif discount == "DISC20":
            subtotal = quantity * price * 0.8
        else:
            subtotal = quantity * price

        total += float(f"{subtotal:.2f}")

        print(f"{i+1}. {food} - Quantity: {quantity}, Unit Price: {price:.2f} TWD, Subtotal: {subtotal:.2f} TWD")

    print(f"Total Cost: {total:.2f} TWD")
    print()